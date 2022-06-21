#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 03
# Problem 5
# 204111 Sec 002

def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    value = int(input('Input digit: '))
    # พิมพ์ตัวเลขหลังจากการเปลี่ยนค่าหลักที่กำหนด
    print(set_kth_digit(number, k, value))

def kth_digit(number, k):
    return (abs(number) // 10**k)% 10
    

def set_kth_digit(number, k, value): 
    #เอาค่าที่จะมาแทนในหน่วยใดๆในค่าnumberมาลบกับหลักๆนั้น
    a = value - (kth_digit(number, k))
    #เอาค่าaที่ได้มาแปลงเป็นจำนวนเต็มในหลักๆนั้น
    b = a*10**k
    #เอาค่าbที่ได้มาบวกกับค่าnumber
    c = b + number
    #จะได้ผลลัพธ์ที่เปลี่ยนเลขในหลักๆนั้น
    return abs(c)

if __name__ == '__main__':
    main()

