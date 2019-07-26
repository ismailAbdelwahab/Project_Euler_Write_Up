#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 23 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        22th Problem : https://projecteuler.net/problem=22
#
# NOTE: The file "names_pb22.txt" must be in the same folder
#    as this python script.
#----------------------------------------------------------------

def alphaSumValue(name):
	""" Give the sum of all alphabetical position of each letter in the "name" """
	alphaSum = 0
	for c in name:
		alphaSum += ord(c)-64
	return alphaSum


def main():
	# Read the file "names_pb22.txt" and get all the names in a list 
	with open("names_pb22.txt","r") as f:
		namesArray = f.read().split("\",\"")

	# Length of the array
	lenArray = len(namesArray)
	# Remove the extra: "   in the first element and the last of the array.
	namesArray[0] = namesArray[0][1:]
	namesArray[lenArray-1] = namesArray[lenArray-1][:-1]
	# Sorting the array
	namesArray.sort()

	totalScore = 0
	index = 1
	for name in namesArray:
		totalScore += alphaSumValue(name) * index
		index += 1

	print("    |#| Project Euler - problem 22 |#|\n")
	print("The total score of this file is:")
	print("   Score =",totalScore)

if __name__ == '__main__':
	main()
