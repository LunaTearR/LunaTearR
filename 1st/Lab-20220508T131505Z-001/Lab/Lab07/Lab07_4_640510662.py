#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 1
# 204111 Sec 002

def main():
    print(life_path(int(input())))

def life_path(n):
    input = n
    sum = 0
    while n > 0: 
        n1=n%10     #Keep the value of the last digit.
        n=n//10     #Remove the last digit.
        sum += n1   #Add the last digit that has been removed.
        #Repeat until sum reach the value more than 9.
        if sum // 10 !=0: #When sum have 2 digits 
            n0 = sum      #Keep new sum in n0
            sum = 0       #Reset the value of sum to 0
            while n0 > 0: 
                n1=n0%10
                n0=n0//10
                sum += n1 #When n0 is equal to 0 go back to the top loop then repeat the loop.
    return sum


if __name__ == '__main__':
    main()