#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019						
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        4th Problem : https://projecteuler.net/problem=4			
#
#  	Largest palindrome from the product of two 3-digit numbers.
#----------------------------------------------------------------

def isPalindrom(n):
	""" Check if n is a palindrom """
	n = str(n)
	inf, sup = 0, len(n)-1
	while(inf < sup and n[inf] == n[sup]):
		inf += 1
		sup -= 1
	return (inf >= sup)

answer = 0
a, b = 999, 999
palin = 0
while ( a > 99 ):
	b = 999
	while (b > 99):
		if( isPalindrom(a*b) ):
			palin = max(a*b, palin)
		b -= 1
	a -= 1

#-------------
#   OUTPUT		
#-------------

print ("The largest palindrome from the product of two 3-digit numbers is :")
print ("   palindrome =", palin)
