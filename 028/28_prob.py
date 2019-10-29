#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: 29 October 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        28th Problem : https://projecteuler.net/problem=28
#----------------------------------------------------------------
from time import time

def main():
	""" The distance between the 4 apex of a square is constant.
	And from a square of size X to the one of size X+1
	this distance (shift in code) is raised by 2. """ 
	total = 1
	actual_nb = 1
	shift = 2
	for _ in range(500): # The square of size _*2-1
		for _ in range(4): #Get the 4 apex of the actual square
			actual_nb += shift
			total += actual_nb
		shift += 2
	print("Total = "+ str(total))

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(time() - start_time))