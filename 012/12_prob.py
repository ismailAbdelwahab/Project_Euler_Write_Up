#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Wrprime_factor_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        12th Problem : https://projecteuler.net/problem=12
#
#     Find the first triangular number that has over 500 divisors.
#----------------------------------------------------------------
from math import sqrt

number = 0          #The number tested
triangle_index = 1  #Used to increment "number" to get the next triangular number
nb_divisors = 2     #Counter of divisors of "number"

while(nb_divisors < 501):
	number += triangle_index
	nb_divisors = 2
	for div in range(2, int(sqrt(number))+1):
		if(number%div == 0):
			if(number/div == div):
				#Special case where div*div == number
				# div has to be counted only ONCE !
				nb_divisors += 1
				continue
			else:
				nb_divisors += 2
	triangle_index += 1
	print("Tested number:",number,",has",nb_divisors,"divisors.")

print("\nThe first triangular number that has over 500 divisors is:")
print("     Triangular number =",number,"with ",nb_divisors,"divisors.")