#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019						
#   https://github.com/ismailAbdelwahab/Project_Euler_Wrprime_factor_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        3nd Problem : https://projecteuler.net/problem=3			
#
#  	Find the largest prime factor of the number 600851475143.
#----------------------------------------------------------------


myNumber = 600851475143 #Target value
value = 1 				#actual value
prime_factor = 1  		#the prime factor tested.

while(value != myNumber):
	prime_factor += 1
	if (myNumber % prime_factor == 0):
		value *= prime_factor

print("The largest prime factor of the number 600851475143 is :")
print("    Largest prime factor = ",prime_factor)