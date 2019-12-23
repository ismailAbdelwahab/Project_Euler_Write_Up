#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 23 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        13th Problem : https://projecteuler.net/problem=13
#
#     10 first digits of the sum of all numbers in bigNumber.txt.
#----------------------------------------------------------------


# Get the numbers in a list:
with open("bigNumber.txt","r") as f:
	numbers = f.read().split("\n")

# Convert all string_number into int:
numbers = [int(i) for i in numbers]

#-------------
#   OUTPUT	
#-------------
print ("  The first 10 digits of the sum of all these numbers are :")
print("   Sum =  " + str(sum(numbers))[0:10] )