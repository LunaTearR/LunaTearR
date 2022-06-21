#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 04
# Problem 5
# 204111 Sec 002

def nearest_odd(x):
    xwd = (x*10)//10  #เก็บแค่ค่าที่เป็นจำนวนเต็ม
    
    if xwd % 2 == 0:    #ใช่เงื่อนไขถ้า % แล้วเท่ากับ 0 = เลขคู่ = บวกเพิ่มไป 1 เพื่อให้เป็นจำนวนคี่ที่มากกว่า x
        xwd = xwd + 1    #ถ้า % แล้วไม่เท่ากับ 0 = เลขคี่ = คงค่าเท่าเดิม
    else:
        xwd = xwd
    return int(xwd) 

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(nearest_odd(x))

if __name__ == '__main__':
    main()

#xwd = x without decimal
