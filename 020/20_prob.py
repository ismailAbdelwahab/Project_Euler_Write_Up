#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        20th Problem : https://projecteuler.net/problem=20
#----------------------------------------------------------------
def facto(n):
	""" Return n! """
	factorial = 1
	for x in range (1,n+1):
		factorial *= x
	return factorial

def main():
	number = 100
	factoAsString = str(facto(number))
	sum_of_all_digits = 0
	for digit in factoAsString :
		sum_of_all_digits += int(digit)

	print ("number =",number)
	print ("(number)! =",facto(number),"\n")
	print ("Sum of al digits of ("+str(number)+")! is:")
	print ("   Sum = ",sum_of_all_digits)

if __name__ == '__main__':
	main()