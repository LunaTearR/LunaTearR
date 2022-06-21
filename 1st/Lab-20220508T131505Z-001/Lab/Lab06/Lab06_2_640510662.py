#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 2
# 204111 Sec 002

def float_to_bin(x):
    if x >= 0:
        output = int_to_bin(x) + af_point_to_bin(x)
    else:
        output = (int_to_bin(x) + af_point_to_bin(x))*-1
    return  float('{0:.6f}'.format(output))

def af_point_to_bin(x): #เลขทศนิยม
    result = 0
    i = 1
    x = abs(float(x) - int(x)) #เก็บแค่ค่าทศนิยม
    if x == 0: 
        return 0
    else:
        pass

    while x != 1:
        x = x*2
        r = x//1
        result += r*10**-i #ตำแน่งตัวเลขหลังจุดทศนิยม
        if x > 1 :
            x = x-1
        else :
            x = x
        i += 1
    return result

def int_to_bin(x): #จำนวนเต็ม
    result = 0
    i = 0
    x = int(x) #แปรงค่าเป็นจำนวนเต็ม
    while x != 0:
        r = x%2
        result = result+r*10**i #ตำแหน่งตัวเลขหน้าจุดทศนิยม
        x = int(x/2)
        i += 1
    return result

def main():
    x = float(input())
    print('{0:.6f}'.format(float_to_bin(x)))

if __name__ == '__main__':
    main()
