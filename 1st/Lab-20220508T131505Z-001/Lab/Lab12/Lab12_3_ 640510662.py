#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 12
# Problem 3
# 204111 Sec 002

def main():
	n = int(input())
	print(is_prime(n))

def is_prime(n):
    def prime(n, i = 2): 
        if (n <= 2): 
            if(n == 2):
                return True 
            else: return False
        if (n % i == 0): 
            return False
        if (i * i > n): 
            return True 
        return prime(n, i + 1) 
        
    return prime(n)
if __name__ == '__main__':
	main()