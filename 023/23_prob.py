#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 23 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        23th Problem : https://projecteuler.net/problem=23
#----------------------------------------------------------------
from time import time
from math import sqrt

def sumOfProperDivisors(n):
	""" Return the sum of all proper divisors of n """
	sumOfDivisors = 1
	for i in range(2,int(sqrt(n))+1):
		if (n%i == 0):
			sumOfDivisors += i
			if (n//i != i):
				sumOfDivisors += n//i
	return sumOfDivisors

def isAbundantNumber(n):
	""" n is abundant if the sum of its proper divisor is greater than n """
	return sumOfProperDivisors(n) > n

def getArrayWithAbundantsUnderN(n):
	""" Return an array with all abundants number that are lower to "n"(with "n" included)
		Note: the lowest abundant is 12, the loop starts at 12. """
	abundantsArray = []
	for number in range(12,n):
		if isAbundantNumber(number):
			abundantsArray.append(number)
	return abundantsArray

def isSumOfAbundant(abundants, n):
	""" Return true if "n" can be written as the sum of 2 numbers in the array "abundant"
		Return false otherwise. """
	firstIndex = 0
	lastIndex = len(abundants)-1
	sumOf2Numbers = abundants[firstIndex] + abundants[lastIndex]
	while(sumOf2Numbers != n and firstIndex < lastIndex):
		if( sumOf2Numbers < n):
			firstIndex += 1
		else:
			lastIndex -= 1
		sumOf2Numbers = abundants[firstIndex] + abundants[lastIndex]
	return sumOf2Numbers == n 

def main():	
	result = 0
	#Create the array of all abundant number between 12 and 28123
	abundantsArray = getArrayWithAbundantsUnderN(28123)

	print(" Starting calculating loop ... (1 --> 28123) ")
	for number in range(1,28123):
		if( not isSumOfAbundant(abundantsArray, number) ):
			result += number

		#Print info on the progression on the screen:
		if( not number%2500 ):
			print("All numbers under",number,"have been treated.")
	
	#Final result, OUTPUT:
	print("\nThe sum of all number, that can't be written as the sum of 2 abundant numbers, is :")
	print("    Sum =",result)

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.1f} seconds.\n".format(time()-start_time))