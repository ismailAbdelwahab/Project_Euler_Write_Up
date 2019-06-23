#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        14th Problem : https://projecteuler.net/problem=14
#
#     Give the number (< 1 million) that produces the longuest Collatz sequence.
#----------------------------------------------------------------

def CollatzNextValue(n):
	""" Return the next value of "n" in the Collatz sequence """
	return n/2 if n%2==0 else 3*n+1

def lenOfCollatzSequence(n):
	""" Return the length of the Collatz's sequence on "n" """
	length = 1
	while( n != 1 ):
		n = CollatzNextValue(n)
		length += 1
	return length


def main():
	answer_number = 0
	answer_len = 0

	for numberTested in range(999999,500000,-2):
		length_sequence = lenOfCollatzSequence(numberTested)
		if( length_sequence > answer_len ):
			answer_len = length_sequence
			answer_number = numberTested 
		print("Number tested :",numberTested," with",length_sequence," of length.")

	#-------------
	#   OUTPUT	
	#-------------
	print(" The longest chain has been foud :")
	print("     root = ",answer_number,"  with a length of :",answer_len," values.")


if __name__ == '__main__':
	main()