#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 21 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Wrprime_factor_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        8th Problem : https://projecteuler.net/problem=7
#
#  	  13 adjacent digits with greatest product in a matrix.
#----------------------------------------------------------------

with open("matrix.txt","r") as f:
	#Get all ligns of the text file as 1 string
	text = f.read().replace("\n",'') 

lastIn = len(text)-1
max_prod = 1

for index in range (lastIn-12):
	#Getting the next sequence of 13 digits
	digits_sequence = text[index:index+13]
	#Calculating the product of these 13 digits
	new_prod = 1
	for nb_as_char in digits_sequence:
		new_prod *= int(nb_as_char)
	#Keep in memory the max between previous max and this new product
	max_prod = max(max_prod,new_prod)

#-------------
#   OUTPUT	
#-------------
print ("The max prod of 13 charact in this matrix is :")
print ("    max prod = ",max_prod)
