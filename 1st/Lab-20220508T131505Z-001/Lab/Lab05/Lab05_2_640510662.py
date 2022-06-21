#!/usr/bin/env python3
# นายธีรภัทร์ นิลศิริ
# 640510662
# Lab 05
# Problem 2
# 204111 Sec 002

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(is_p_triple(x, y, z))

def is_p_triple(x, y, z):
    #ค่ามากสุด = ค่า1 + ค่า2 
    max = max_of_3(x, y, z)
    mid = mid_of_3(x, y, z)
    min = min_of_3(x, y, z)
    #c^2 = a^2+b^2
    if (max**2) == (mid**2)+(min**2):
        return True
    else:
        return False

def max_of_3(x, y, z):
    #หาค่าmax จากการเทียบ x กับ y ก่อน
    if x > y:
        max = x
    else: 
        max = y
    #จากนั้นเอาไปเทียบกับ z
    if max > z:
        max = max
    else:
        max = z
    return max

def min_of_3(x, y, z):
    #หาค่าmin จากการเทียบ x กับ y ก่อน
    if x > y :
        min = y
    else: 
        min = x
    #จากนั้นเอาไปเทียบกับ z
    if min > z: 
        min = z
    else:
        min = min 
    return min

def mid_of_3(x, y, z) : #หาค่าตรงกลางจากการคิดทุกกรณีที่เป็นไปได้
    if x >= y >= z or z >= y >= x :
        return y
    if x >= z >= y or y >= z >= x :
        return z
    if y >= x >= z or z >= x >= y :
        return x 

if __name__ == '__main__':
    main()
