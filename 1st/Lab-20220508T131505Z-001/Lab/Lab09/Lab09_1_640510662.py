#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 09
# Problem 1
# 204111 Sec 002

def main():
	x = [[-8, 29, 24, 20, 16, 11, 14, 12, 19], [28, -7, 6, 15, 25, 47, 0, 49, 9], [14, 49, 32, -8, -7, 21, 2, -2, -8]]

	y = [[-10, 30, 5, -1, 43, 8, 25, 8], [22, 2, 22, 43, -2, 43, 33, 29], [21, 30, 33, 36, 23, 20, 15, 20], [31, 42, 13, 15, -9, 0, 12, 30], [-7, 5, 46, 38, 6, -8, -7, 10], [-10, 40, 17, -10, 49, 8, 32, -10], [16, 29, -2, 32, 39, 23, 45, 2], [32, -5, 39, 6, 10, 36, 8, -7], [8, 30, 15, 41, 46, 21, -9, 28]]
	print (matrix_mult(x,y))

def check_matrix(m1, m2):
	if (len(m1[0])) == (len(m2)): #Check matrix
		return True
	else:
		return None

def matrix_mult(m1, m2):
	
	result = [[0 for row in range(len(m2[0]))] 
					for col in range(len(m1))] 
	
	if check_matrix(m1, m2) is True:
		for i in range(len(m1)):
			for j in range(len(m2[0])):
				for k in range(len(m2)):
					result[i][j] += m1[i][k]*m2[k][j]
		return result 
	else:
		return None

if __name__ == '__main__':
    main()
