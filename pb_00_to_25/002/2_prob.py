#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019						
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        2nd Problem : https://projecteuler.net/problem=2				
#
#  	Sum of Fibonacci's even values that does not exceed 4 million.
#----------------------------------------------------------------

def nextEvenFiboValue(array):
	""" Put the next even value, of the fibonacci sequence, in array[2] """
	for _ in range(3):
		array[0], array[1] = array[1], array[2]
		array[2] = array[0] + array[1]

# NOTE: fibo[] is as:  fibo[0] + fibo[1] = fibo[2]
# NOTE: 4e6 <==> 4000000

answer  = 0
fibo = [1,1,2]
while fibo[2] < 4e6 :
	answer += fibo[2]
	nextEvenFiboValue( fibo )

#-------------
#   OUTPUT		
#-------------
print("The sum of Fibonacci's even values that does not exceed 4 million is :")
print("		sum = ", answer)
	