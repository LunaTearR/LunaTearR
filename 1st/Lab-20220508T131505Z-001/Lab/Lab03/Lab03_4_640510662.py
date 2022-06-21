#!/usr/bin/env python3
# ธีรภัทร์ นิลศฺิริ
# 640510662
# Lab 03
# Problem 4
# 204111 Sec 002

def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    # พิมพ์ตัวเลขตำแหน่งที่ k ของข้อมูลเข้า
    print(kth_digit(number, k))

def kth_digit(number, k):
    return (abs(number) // 10**k)% 10

if __name__ == '__main__':
    main()