#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        16th Problem : https://projecteuler.net/problem=16
#
#  	  Sum of all digit of 2**1000.
#----------------------------------------------------------------
def get_sum_of_digits_from_string( string ):
	sum_of_digit = 0
	for char in string:
		sum_of_digit += int(char)
	return sum_of_digit

def main():
	nb = 2**1000
	nb_string = str(nb)
	digits_sum = get_sum_of_digits_from_string( nb_string )
	#-------------
	#   OUTPUT	
	#-------------
	print ("The sum of all digits of the number 2**1000 is :")
	print( "    Sum = ", digits_sum)

if __name__ == '__main__':
	main()