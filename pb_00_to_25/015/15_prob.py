#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 21 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        15th Problem : https://projecteuler.net/problem=15
#
#   Find the number of path in a 20*20 grid by going right and down only.
#----------------------------------------------------------------

def factorial(n):
	""" Return  n! """
	return 1 if (n==1) else n*factorial(n-1)

def n_choose_k( n, k ):
	""" Return:  n! /( k!(n-k)! ) """
	if (n == k):
		return 1
	return int(   factorial(n)/( factorial(k)*factorial(n-k) )    )

def main():
	#-------------
	#   OUTPUT	
	#-------------
	print("The possible paths have been calculated for a grid 20*20")
	print("   Number of paths possible =",n_choose_k(40,20))

if __name__ == '__main__':
	main()
