#!/usr/bin/env python3
#----------------------------------------------------------------
#  Made by ABDEL WAHAB Ismail.      Created: Jully 22 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Write_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        18th Problem : https://projecteuler.net/problem=18
#----------------------------------------------------------------

def nb_elements_on_previous_lines(myLine):
	"""Get the number of ALL elements from line 1 to line "myLine-1" """
	nb_elems= 0;
	for i in range (1,myLine):
		nb_elems += i
	return nb_elems

def get_line_from_index(index):
	""" Get the number of the line we are on based on the index of the number in the tree """
	nb_elems = 0;
	line = 1;
	while (nb_elems < index):
		nb_elems += line
		line+=1
	return line-1

def get_left_child_index(index):
	""" Get the left child of an element at the index 'index' in the tree """
	line = get_line_from_index(index)
	if(line == 15):
		return -1
	nb_elems_passed = nb_elements_on_previous_lines(line)
	index_in_line = index - nb_elems_passed
	index_left_child = nb_elems_passed + line +index_in_line
	return index_left_child

def find_highest_sum(tree,index):
	""" recusiv function that calculate the maximum sum found on the index we are on """
	i_left_child = get_left_child_index(index)
	i_right_child = i_left_child+1
	if(i_left_child !=-1):
		max_from_childs = max(find_highest_sum(tree,i_left_child),\
							  find_highest_sum(tree,i_right_child))
	else:
		return tree[index]
	return tree[index] + max_from_childs

def main():
	"""Root of the tree is: tree[1]. (Please ignore tree[0])"""
	tree = [0, 75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4,\
	 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7,\
	 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56,\
	 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94,\
	 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, \
	 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, \
	 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, \
	 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, \
	 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

	print("The maximum sum from top to bottom in this triangle is:")
	print("     ----> Max sum = ",find_highest_sum(tree,1),".")
	
if __name__ == '__main__':
	main()