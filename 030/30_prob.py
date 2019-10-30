#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: October 30 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        30th Problem : https://projecteuler.net/problem=30
#----------------------------------------------------------------
from time import time

def sumFifthPower(n):
	""" Return the sum of all digits of n raised to the power of 5 """
	total = 0
	for c in str(n):
		total += int(c)**5
	return total

def main():
	result = 0
	#1 million as an upper born was choosen randomly but is enough to find the solution
	for n in range (10,1000000):
		if( n == sumFifthPower(n)):
			result += n
	print("Sum of all numbers that can be written\n\
	 as the sum of Fifth powers of their digits is: "+ str(result))

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(time() - start_time))
