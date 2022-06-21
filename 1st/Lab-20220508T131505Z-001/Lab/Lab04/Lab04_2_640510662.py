#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 04
# Problem 2
# 204111 Sec 002

def main():
    # receive input from user
    a = int(input())
    b = int(input())
    c = int(input())
    # call function
    my_max_mid_min(a, b, c)

def my_max_mid_min(a, b, c):
    max = max_of_3(a, b, c)
    mid = mid_of_3(a, b, c)
    min = min_of_3(a, b, c)

    print ("max = {0}" 
        "\nmid = {1}" 
        "\nmin = {2}" .format(max, mid, min))

def max_of_3(a, b, c):
    #หาค่าmax จากการเทียบ a กับ b ก่อน
    if a > b:
        max = a
    else: 
        max = b
    #จากนั้นเอาไปเทียบกับ c
    if max > c:
        max = max
    else:
        max = c
    return max

def min_of_3(a, b, c):
    #หาค่าmin จากการเทียบ a กับ b ก่อน
    if a > b :
        min = b
    else: 
        min = a
    #จากนั้นเอาไปเทียบกับ c
    if min > c: 
        min = c
    else:
        min = min 
    return min

def mid_of_3(a, b, c) : #หาค่าตรงกลางจากการคิดทุกกรณีที่เป็นไปได้
    if a >= b >= c or c >= b >= a :
        return b
    if a >= c >= b or b >= c >= a :
        return c
    if b >= a >= c or c >= a >= b :
        return a 

if __name__ == '__main__':
    main()