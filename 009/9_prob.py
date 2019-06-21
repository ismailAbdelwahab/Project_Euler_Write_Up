#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 21 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Wrprime_factor_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        9th Problem : https://projecteuler.net/problem=9
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc
#----------------------------------------------------------------

for a in range(1000): #first number:
	b = a+1           #second number  b > a
	c = 1000 - a - b  #third number   c is the rest of the substration of a and b on 1000
	while( b < c ):
		if( a+b+c == 1000 and a**2 + b**2 == c**2 ):
			print ("This is a, b and c :")
			print ("a = ",a,", b = ",b,", c = ",c,".")
			print ("a*b*c = ",a*b*c)
			break
		b += 1   #increase b
		c -= 1   #decrease c
		#Retest.
# When the result is found we break: The program  output the result and stops.	
