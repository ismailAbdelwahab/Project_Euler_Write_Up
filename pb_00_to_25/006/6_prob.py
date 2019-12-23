#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019						
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        6th Problem : https://projecteuler.net/problem=6			
#
#  	Difference between the "sum of the squares" and "the square of the sums" 
#     with the first 100 natural numbers.
#----------------------------------------------------------------


def sumOfSquares(num):
	return (2*num+1)*(num+1)*num/6

def squareOfSums(num):
	sumNb = 0
	for i in range(1,num+1):
		sumNb += i
	return sumNb**2 

if __name__ == "__main__":	
	sum_of_squares = sumOfSquares(100)  # a² + b² + c² ...

	square_of_sum = squareOfSums(100)   # (A + B + C ...)²

	result = int(square_of_sum - sum_of_squares)
	#-------------
	#   OUTPUT		
	#-------------

	print ("Difference between the \"sum of the squares\" and \"the square of the sums\"\n \
	with the first 100 natural numbers:")
	print ("   result = ",result)
