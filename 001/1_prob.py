#!/usr/bin/env python3
#################################################################
#            Copyright (c) ABDEL WAHAB Ismail.					#
#	               Created: June 19 2019						#
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	#
#################################################################

#################################################################
#              First problem of  Project Euler:					#
#			  https://projecteuler.net/problem=1				#
#           													#
#						Question:								#
#  	  Find the sum of all the multiples of 3 or 5 below 1000.	#
#################################################################

multiples = [i for i in range(1000) if i%3==0 or i%5==0]
sum_multiples = sum( multiples )

#################
#    OUTPUT		#
#################
print("The sum of all multiples of 3 or 5 below 1000 is:")
print("   Sum =",sum_multiples)

#NOTE: 1000 is exluded. So we do not add it in our answer.