#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019						
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        5th Problem : https://projecteuler.net/problem=5
#
#  	Smallest int evenly divisible by all numbers from 1 to 20.
#----------------------------------------------------------------

def isGood(num):
	""" Checks if num is divisible by 11 up to 20 """
	for i in range(11,21):
		if (num % i != 0):
			return False
	return True

if __name__ == "__main__":	
	number = 19*17*13*11*7*5*3*2
	value = number

	while (not isGood(value)):
		value += number

	#-------------
	#   OUTPUT	
	print ("The smallest int evenly divisible by all numbers from 1 to 20 is :")
	print ("   smallest int = ",value ) 	
	#-------------