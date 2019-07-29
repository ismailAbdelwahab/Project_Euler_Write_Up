#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 28 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        24th Problem : https://projecteuler.net/problem=24
#----------------------------------------------------------------
from time import time

def factorial(n):
    """ Return n! """
    if(n==0 or n==1):
        return n
    return factorial(n-1) * n

def getNextRemainder(permu, factoArr):
    """ Return a tuple as: (indexOfNextDigit, remainderOfDiv)
    we make the division between permu and the first factorial
    that is lower(or equal) to permu."""
    index = 0
    while( index < len(factoArr)-1 and factoArr[index] < permu ):
        index += 1
    index -=1 # we need the index to point a lower number than permu    
    indexOfNextDigit = permu // factoArr[index]
    remainderOfDiv = permu % factoArr[index]
    if( not remainderOfDiv):
        indexOfNextDigit -= 1
    return (indexOfNextDigit , remainderOfDiv) 

def main():
    answer = 0
    # 1| get factorial list:
    factoArr = [factorial(x) for x in range(1,11)]

    # 2| Create an array with all digits in the substitution
    digitArr = [x for x in range(10)]
 
    # 3| init remainder varible used in loop:
    remainder = (0, 1000000)
    while( digitArr ):
        remainder = getNextRemainder(remainder[1], factoArr)
        # 4| Get the index of the next digit
        indexOfNextDigit = remainder[0]
        # 5| Get the next digit from the array "digitArr" (and removes it)
        nextDigit = digitArr[indexOfNextDigit]
        del digitArr[indexOfNextDigit]
        # 6| add it to out answer:
        answer = answer*10+nextDigit if answer!=0 else nextDigit

    print("\n  |#|  Project Euler: problem 24|#|\n")
    print(" The 1 000 000'th substition of [0:9] is: ")
    print("   Found substitution:",answer)

    # 7| Check real answer:
    millionthSubstitution =  2783915460 
    print("        EXPECTED     :",millionthSubstitution)

if __name__ == '__main__':
	start_time = time()
	main()
	print("\n # Execution time: {:.1f} seconds.\n".format(start_time - time()))
