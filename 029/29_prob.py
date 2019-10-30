#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: 30 October 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        29th Problem : https://projecteuler.net/problem=29
#----------------------------------------------------------------
from time import time

def uniqueInArray( array ):
	""" keep only one occurrence of each element in array """
	uniqueArray = []
	for element in array:
		if( element not in uniqueArray ):
			uniqueArray .append( element )
	return uniqueArray 


def nbOfDistinctElements( array ):
	""" Return the length of the array with on distinct elements as a String """
	return str( len( uniqueInArray(array) ) )

def main():
	numbers = [a**b for a in range(2,101) for b in range(2,101)]
	print("The number of distinct element on a**b with 2 <= a,b <= 100 is:")
	print("nb of elements : "+ nbOfDistinctElements(numbers))

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(time() - start_time))
