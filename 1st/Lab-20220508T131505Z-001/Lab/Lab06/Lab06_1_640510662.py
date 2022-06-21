#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 1
# 204111 Sec 002

def int_power(x, y):  
    for i in range(1): #start from 1     
        if y < 0:      #if power is negative
            return 1 / int_power(x, -y) #1/2^x
        elif y > 0:    #if power is positive
            return x * int_power(x, y - 1) 
        else:          #if power is equal to 0
            return 1 

def main():
    x = float(input())
    y = int(input())
    print("{:.6f}".format(int_power(x,y)))
    

if __name__ == '__main__':
    main()