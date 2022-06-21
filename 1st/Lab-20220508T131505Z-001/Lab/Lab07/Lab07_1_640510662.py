#!#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 1
# 204111 Sec 002
import math 
def main():
    x  = int(input("from number:"))
    y  = int(input("to number"))
    prime_in_range(x, y)
    
def is_prime(x):                #Use the function to check whether that number is prime or not?
    div = 2
    while div <= math.sqrt(x):
        if x % div == 0:
            #print (x,'False')
            return False
        else:
            if div == 2:
                div = 3
            else:
                div = div + 1
    #print (x,'True')
    return True

def sum_prime_in_range(x, y):
    sum = 0                     #Sum star at 0
    for i in range(x, y+1 ,1):  #Start checking from x to y (including x and y). 
        prime = is_prime(i)     #We use i because we want to check the number in range between x and y if any of the number in that range is prime. We keep it, and add them together.
        if (prime):             #If which of number in that range is prime keep it and sum them together.
            sum = sum + i       #Then we add all of the prime number in range x and y.


    return sum

def prime_in_range(x,y):
    print (sum_prime_in_range(x, y))
        
if __name__ == '__main__':
    main()
