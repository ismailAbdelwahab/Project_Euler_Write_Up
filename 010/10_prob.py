#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: 31 October 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up 	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        10th Problem : https://projecteuler.net/problem=10
#----------------------------------------------------------------
from time import time

def isPrime(n):
	""" 
		Check if a number is prime or not.
	 	2 and 3 are prime.
	 	if n is divisible by 2 or 3, then n is not prime
	 	else we try all divisors "i"(of type 6k-1 or 6k+1) 
	 		if i*i <= n            (with k a prime number)
	"""
	if(n==2 or n==3):
		return True
	if(n%2 == 0 or n%3 == 0):
		return False
	i = 5
	while(i*i <= n):
		if(n%i == 0 or n%(i+2) == 0):
			return False
		i += 6
	return True

def main():
	sum_of_primes = 2

	for number in range(3,2000000,2):
		if( isPrime( number ) ):
			sum_of_primes += number
			print ("number added: "+str(number)+".")

	print ("The sum of all prime numbers below 2 million is :")
	print ("     sum =",sum_of_primes,".")

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(time() - start_time))