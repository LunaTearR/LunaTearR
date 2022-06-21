#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 11
# Problem 5
# 204111 Sec 002

def main():
	list_x = [19, 48, 175, 290, 873, -7, 43, 69]
	radix_int(list_x)
	print('--------')
	print(list_x)

def radix_int(list_x):
	#This loop is for removing negatives from list of numbers.
	for i in list_x:
		if i >= 0:		
			pass
		else:		#remove the number that less than zero.
			list_x.remove(i)
	#Sort numbers in list.
	list_x.sort()

if __name__ == '__main__':
	main()