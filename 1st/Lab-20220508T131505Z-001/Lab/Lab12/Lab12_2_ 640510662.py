#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 12
# Problem 2
# 204111 Sec 002

def main():
    n = int(input())
    num = int(input())
   
    print(n_base_to_10(n,num))	 

def n_base_to_10(n, num):
    if num == 0:
        return 0
    else:
        return (num% 10) + (n* n_base_to_10(n,num // 10))

    '''
    if n == 2:
        if num==0:
            return 0
        else:
            return (num% 10 + 2* n_base_to_10(n,num // 10)) 
    if n == 4:
        if num == 0:
            return 0
        else:
            return (num%10 + 4*n_base_to_10(n,num // 10)) 
    if n == 8:       
        if num == 0:
            return 0
        else:
            return (num%10 + 8*n_base_to_10(n,num // 10)) 
    '''

    
if __name__ == '__main__':
	main()