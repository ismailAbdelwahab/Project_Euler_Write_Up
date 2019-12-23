#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        20th Problem : https://projecteuler.net/problem=20
#----------------------------------------------------------------
from time import time
from math import sqrt

def findDivisors(n):
	""" Return an array all divisors of n (Warning: n is not included here!) """
	arrayDivisorsEven = [1]
	for i in range(2,int(sqrt(n))+1):
		if (n%i == 0):
			arrayDivisorsEven.append(i)
			if (n//i != i):
				arrayDivisorsEven.append(n//i)
	return arrayDivisorsEven

def SumElementInArray(array):
	""" Return the sum of an array """
	return sum(array)

def checkAmicableNumber(n,divSum):
	""" Return true if "n" and "divSum" are amicable number. """
	if (n == divSum):
		return False
	arrayOfDivisors = findDivisors(divSum)
	sumOfDivisors = SumElementInArray(arrayOfDivisors)
	return (sumOfDivisors == n)

def addAmicableNumbers(amicablesArray,n,divSum):
	""" Append to amicablesArray the numbers "n" and "divSum" """
	amicablesArray.append(n)
	amicablesArray.append(divSum)

def main():
	#Array of all amicables found
	amicables = []
	#Array of all divisors found for the actual "number"
	arrayOfDivisors = []
	#Sum of the previous array
	sumOfDivisors = 0

	for number in range (1,10000):
		if(number in amicables): # Skip the number
			continue
		#Get divisors and calculate their sum
		arrayOfDivisors = findDivisors(number)
		sumOfDivisors = SumElementInArray(arrayOfDivisors)
		#Check the amicable possible numbers
		if checkAmicableNumber(number,sumOfDivisors):
			addAmicableNumbers(amicables,number,sumOfDivisors)
		print("Number done :",number,".")

	amicablesSum = SumElementInArray(amicables)

	print("\n    |#| Project Euler - problem 21 |#|\n")
	print("Amicables array :",amicables,"\n")
	print("Sum of all amicable number below 10000 is :")
	print("   Number of amicables found = ",len(amicables))
	print("   Sum of them = ",amicablesSum)


if __name__ == '__main__':
	start_time = time()
	main()
	print("\n Execution time: {:.2f} seconds".format(time()-start_time))
