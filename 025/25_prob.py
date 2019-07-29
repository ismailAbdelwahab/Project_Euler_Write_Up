#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 29 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        25th Problem : https://projecteuler.net/problem=25
#----------------------------------------------------------------
from time import time

def nextFiboNumber(fiboArr):
    """ 1 - Set fiboArr[2] as the next fibonacci number 
        2 - And increment fiboArr[3] which is the fibonacci index
        of fiboArr[2]"""
    fiboArr[0] = fiboArr[1]
    fiboArr[1] = fiboArr[2]
    fiboArr[2] = fiboArr[0] + fiboArr[1]
    fiboArr[3] += 1

def main():
    fiboArr = [0,1,1,2]
    while( len(str(fiboArr[2])) < 1000 ):
        nextFiboNumber(fiboArr)
    
    print("\n |#| Project Euler : problem 25 |#|\n")
    print("The index of the first fibonacci number with at least 1000 digits is:")
    print("   index =",fiboArr[3])

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.2f} seconds.\n".format(start_time - time()))
