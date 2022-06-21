#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 12
# Problem 5
# 204111 Sec 002

def main():
    num = int(input())
    print(reverse_num(num))
    
def reverse_num(num): 
    def reverse_helper(num, remainder=0):
        if num == 0:
            return remainder
        elif num<10:
            return reverse_helper(num//10, (remainder+(num%10)))
        else:
            return reverse_helper(num//10, (remainder+(num%10))*10)
    return reverse_helper(num)    
    
if __name__ == '__main__':
    main()