#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: 29 October 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        27th Problem : https://projecteuler.net/problem=27
#----------------------------------------------------------------

from time import time

def primesUpTo999():
	primes = [2]
	n = 3
	while(n < 1000):
		if (isPrime(primes, n) ):
			primes.append(n)
		n += 1
	return primes

def isPrime(primes, n):
	for prime in primes:
		if (prime != n and n % prime == 0):
			return False
	return True

def resizePrimeArray(primes, n):
	last_prime = primes[ len(primes)-1 ]
	while (last_prime <= n):
		last_prime += 2
		if( isPrime(primes,last_prime) ):
			primes.append(last_prime)

def calculateQuadraticAB(primes, a, b, n):
	""" Calculate the value of n² + an + b """
	quad = n**2 + a*n + b
	resizePrimeArray(primes, quad)
	return  quad

def maxPrimeProduced(primes, a,b):
	n = 0
	counter = 0
	test_number = calculateQuadraticAB(primes, a, b, n)
	while ( isPrime(primes, test_number) ):
		n += 1
		counter += 1
		test_number = calculateQuadraticAB(primes, a, b, n)
	return counter


def solution():
	maximum = 0
	a_max = 0
	b_max = 0
	prime_numbers = primesUpTo999()
	for a in range(-999,999):
		for b in primesUpTo999():
			nb_prime = maxPrimeProduced(prime_numbers, a,b)
			if ( nb_prime > maximum ):
				maximum = nb_prime
				a_max = a
				b_max = b
		print( "a: " +  str(a) + " is treated. We foud "+str(nb_prime)+" primes")
	print("Max primes generated :" + str(maximum))
	print("With: a = "+str(a_max) + " b = "+ str(b_max))
	return a_max*b_max

def main():
	print( solution() )


if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(time() - start_time))