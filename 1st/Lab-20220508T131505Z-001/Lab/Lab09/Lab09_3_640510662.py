#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 09
# Problem 3
# 204111 Sec 002

import copy
def main():
	list_magic =[[12, 14, 7, 1],
 				[9, 4, 15, 6],
 				[8, 13, 2, 11],
 				[5, 3, 10, 16]]
	print(is_magic_square(list_magic))	

def find_magic_num(board): #Find the magic number of magic square.
	magic_num = 0
	for i in board[0]:	
		magic_num += i
	return magic_num

def check_num_pow2(board):	#Check each number in the list if it more than the size of square or not.
    num_pow2 = (len(board))**2
    square = copy.deepcopy(board)
    join_list = [j for i in square for j in i] #join all list of list into single list.
    for i in join_list:
        if i > num_pow2:
            return False
    return True

def check_dup_num(board): #Check each number in the list if it duplicate or not.
	square = copy.deepcopy(board)
	join_list = [j for i in square for j in i]

	if len(join_list) != len(set(join_list)):
		return False #When the list have duplicate numbers.
	else:
		return True #When the list don't have duplicate numbers.

def find_columns(board): #Sum all number in columns, then check is it equal to magic number or not.
	magic_num = find_magic_num(board)
	#col_sum = 0
	for i in range(len(board)):
		col_sum = 0
		for j in range(len(board)):
			col_sum += board[j][i]
		if col_sum != magic_num:
			return False
		#else: 
			#return False
	return True

def find_rows(board): #Sum all number in rows, then check is it equal to magic number or not.
	magic_num = find_magic_num(board)
	#row_sum = 0
	for i in range(len(board)):
		row_sum = 0
		for j in range(len(board)):
			row_sum += board[i][j]
		if row_sum != magic_num:
			return False
		#else: 
			#return False
	return True


def find_diagonals_L2R(board): #Sum all number in diagonals from top left to bottom right, then check is it equal to magic number or not.
	magic_num = find_magic_num(board)
	dia_sum = 0
	#TopLeft to BotRight
	for i in range(len(board)):
		dia_sum += board[i][i]
	if dia_sum != magic_num:		
		return False	
	return True
	#TopRight to BotLeft

def find_diagonals_R2L(board): #Sum all number in diagonals from top right to bottom left, then check is it equal to magic number or not.
	magic_num = find_magic_num(board)
	dia_sum = 0
	for i in range(len(board)):
		dia_sum += board[i][-(i+1)]
	if dia_sum != magic_num:
		return False
	return True

def is_magic_square(board):
	if ((check_dup_num(board) and check_num_pow2(board)) is True and 
		(find_columns(board) and find_rows(board)) is True and 
	    (find_diagonals_L2R(board) and find_diagonals_R2L(board)) is True):
		return True
	else:
		return False
 
if __name__ == '__main__':
	main()