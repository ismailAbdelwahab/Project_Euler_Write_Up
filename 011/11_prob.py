#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        11th Problem : https://projecteuler.net/problem=11
#
#     Greatest product of 4 adjacent numbers in a matrix in any direction.
#----------------------------------------------------------------

def horizontalHighest (matrix):
	""" Find the Highest horizontal product in the matrix """
	highestProd = 1
	myLine = 0
	#While there is still a line
	while (myLine < 20):
		#For each starting possible int (from index 0 to 20-4=16)
		for index in range(w-3): 
			actualProd = 1
			#make calculs on this number and the 3 nexts.
			for group in range(4): 
				actualProd *= matrix[myLine][index+group]
			#Keep in memory the highest product ever found here:
			highestProd = max(highestProd, actualProd)
		myLine +=1
	return highestProd

def verticalHighest (matrix):
	""" Find the Highest vertical product in the matrix """
	highestProd = 1
	myColumn = 0
	#While there is still a line
	while myColumn < 20: 
		#for each starting possible int (from 1st to 16st) 
		for index in range(w-3):   
			actualProd = 1
			#make calculs on this number and the 3 nexts.
			for group in range(4): 
				actualProd *= matrix[index+group][myColumn]
			#Keep in memory the highest product ever found here:
			highestProd = max(highestProd, actualProd)
		myColumn +=1
	return highestProd

def diagBottomRightHighest(matrix):
	""" Find the Highest diagonal product in the matrix 
		    # O O O
			O # O O
			O O # O     Diagonal that follow that shape."""
	highestProd = 1
	myLine = 0
	#While there is still a line
	while myLine < 17:
		#for each starting possible int (from 1st to 16th)
		for index in range(w-3):   
			actualProd = 1
			#make calculs on this number and the 3 nexts.
			for group in range(4): 
				actualProd *= matrix[index+group][myLine+group]
			#Keep in memory the highest product ever found here:
			highestProd = max(highestProd, actualProd)
		myLine += 1
	return highestProd

def diagBottomLeftHighest(tab):
	""" Find the Highest diagonal product in the matrix 
			O O O #
			O O # O
			O # O O     Diagonal that follow that shape."""
	highestProd = 1
	myColumn = 19
	#While there is still a line
	while myColumn >= 3:
		#for each starting possible int (from 16th to 4th)[15 -> 3th indexes]
		for index in range(17):
			actualProd = 1
			#make calculs on this number and the 3 previous in diag.[-3,-2,-1,0]
			for group in range(4): 
				actualProd *=tab[index+group][myColumn-group]
			#Keep in memory the highest product ever found here:
			highestProd = max(highestProd, actualProd)
		myColumn -= 1
	return highestProd


#The dimension of our matrix (here 20x20)
h, w = 20, 20 
#Our matrix : 2 dimensionnal array
matrix = [[0 for x in range(w+1)] for y in range(h+1)]

#Get data from text file.
with open("matrix_11_prob.txt","r") as f:
	lines_of_matrix = f.read().split("\n")

#Fill our matrix
NB_line = 0
for lineString in lines_of_matrix:     #Separate each line ("\n")  <- new lines
	NB_column = 0
	for num_as_string in lineString.split(" "):  #Separate each number (" ") <- spaces
		matrix[NB_line][NB_column]=(int(num_as_string))
		NB_column +=1
	NB_line +=1


#-------------
#   OUTPUT	
#-------------
maxHoriz = horizontalHighest(matrix)
print ("Max   in  Horizontal = ",maxHoriz)

maxVert = verticalHighest(matrix)
print ("Max   in  Vertical   = ",maxVert)

maxDiagRight = diagBottomRightHighest(matrix)
print ("Max diag bottom Right= ",maxDiagRight)

maxDiagLeft = diagBottomLeftHighest(matrix)
print ("Max diag bottom Left = ",maxDiagLeft)

realMax = max(maxHoriz, maxVert, maxDiagRight, maxDiagLeft)

print ("\nThe max found by multiplying 4 adjacent number in this matrix is :")
print ("    max = ",realMax,"\n")