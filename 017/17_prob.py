#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        17th Problem : https://projecteuler.net/problem=17
#----------------------------------------------------------------
def main():
	dico = { 0 :"zero" , 1 :"one"  ,   
			 2 :"two"  , 3 :"three", 
			 4 :"four" , 5 :"five" , 
			 6 :"six"  , 7 :"seven",
			 8 :"eight", 9 :"nine",10:"ten",
			 11:"eleven",12:"twelve",
			 13:"thirteen",15:"fifteen",18:"eighteen",
			 20:"twenty", 30:"thirty",
			 40:"forty",50:"fifty", 80:"eighty" }

	completeString = "onethousand"
	"""
	We writte a number as: 999 >= number >= 1
	      and number is of shape:  XYZ

	with X the hundreds , Y the tenths, Z the units
	Each letter represent a digit (0 -> 9) (zero not excluded)

	For example: number = 46 
	Will be represented by X=0, Y=4, Z=6
	Making: 046
	"""
	for hundred in range(9,-1,-1):      # This is X
		for tenth in range(9,-1,-1):    # This is Y
			for unit in range(9,-1,-1): # This is Z
				#Handle X
				if(hundred != 0):
					completeString += dico[hundred] + "hundred"
				
				#Handle the transition between X and (Y or Z)
				if(hundred != 0 and(tenth!=0 or unit!=0)):
					completeString += "and"

				#Handle Y
					#Handle the special cases: 20,30,40,50,80
				if(tenth in [2,3,4,5,8]): 
					completeString += dico[tenth*10]
					#Handle the special cases: 10 -> 19
				elif(tenth == 1):
					if(unit in [0,1,2,3,5,8]): 
						completeString += dico[tenth*10 + unit]
					else:
						completeString += dico[unit]+"teen"
					continue #Do not finish this loop got to the next number directly
				else:
					if(tenth != 0):
						completeString += dico[tenth] + "ty"

				#Handle Z
				if( unit != 0):
					completeString += dico[unit]

	# Print the final result
	print("Length of all the number between 1 and 1000 written is:")
	print("   Length = ",len(completeString))

if __name__ == '__main__':
	main()