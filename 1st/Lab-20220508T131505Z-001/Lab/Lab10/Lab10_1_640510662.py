#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 10
# Problem 1
# 204111 Sec 002

def main():
	n = int(input())
	square_frame(n, sep= '.')


def square_frame(n, sep= ' '):
	num = n
	n_list=[[0 for x in range(num)] for y in range(num)]
	n=1 
	low=0 
	high=num-1
	count = int((num+1)/2)
	for i in range(count):
	    for j in range(low, high+1):
	        if n < 10:
	            n_list[i][j]="0"+str(n)
	        else:
	            n_list[i][j]=n
	        n=n+1
	        
	    for j in range(low+1, high+1):
	        if n < 10:
	            n_list[j][high]="0"+str(n)
	        else:
	            n_list[j][high]=n
	        n=n+1

	    for j in range(high-1, low-1,-1):
	        if n < 10:
	            n_list[high][j]="0"+str(n)
	        else:
	            n_list[high][j]=n
	        n=n+1
	    for j in range (high-1, low,-1):
	        if n < 10:
	            n_list[j][low]="0"+str(n)
	        else:
	            n_list[j][low]=n
	        n=n+1
	    low=low+1
	    high=high-1



	result = (num*num) - int((num-2)*(num-2))
	#print(result)
	for i in range(num):
	    for j in range(num):
	        if int(n_list[i][j]) <= result :
	            if j < num-1:
	                print(n_list[i][j], end=sep)
	            else:
	                print(n_list[i][j], end='') 
	        else:
	            if i <= num-1:
	                print(sep+sep, end=sep)
	            else:
	                print(sep+sep, end=sep)

	    print()


if __name__ == '__main__':
	main()