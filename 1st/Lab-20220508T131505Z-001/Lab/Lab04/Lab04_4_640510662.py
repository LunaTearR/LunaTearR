#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 04
# Problem 4
# 204111 Sec 002

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print (round_to_int(x))

def round_to_int(x):
    if x >= 0:
        x = if_x_is_positive(x)
    if x < 0:
        x = if_x_is_negative(x)
    return int(x)
 
def if_x_is_positive(x):#กรณี x >= 0 
    #ย้ายทศนิยมมาไว้หลักหน่วย
    x_deci = (x*10)
    #เอาค่า x ที่ย้ายทศนิยมมาอยู่หลักหน่วยแล้ว % เพื่อเก็บค่าทศนิยม
    x_move_deci = (x_deci% 10)
    #เก็บแค่ค่าที่เป็นจำนวนเต็ม
    x_without_deci = (x*10)//10
    #ใช่เงื่อนไขในการปัดเศษ ถ้าเศษ >= 5 ปัดเลขขึ้น
    if x_move_deci >= 5 : 
        x_move_deci = x_without_deci + 1
    #เศษ < 5 ปัดลง
    else: x_move_deci = x_without_deci + 0
    #แสดงค่าที่ปัดเศษแล้ว
    return int(x_move_deci) 

def if_x_is_negative(x):#กรณี x < 0 (ค่าติดลบ)
    #ย้ายทศนิยมมาไว้หลักหน่วย #ใส่absให้ x เพื่อให้เป็นค่าบวกเวลาคิดจะง่ายขึ้น
    x_neg = (abs(x)*10 )
    #เอาค่า x ที่ย้ายทศนิยมมาอยู่หลักหน่วยแล้ว % เพื่อเก็บค่าทศนิยม
    x_neg_move_deci = x_neg%10 
    #เก็บแค่ค่าที่เป็นจำนวนเต็ม
    x_neg_without_deci = (abs(x)*10)//10
    #ใช่เงื่อนไขในการปัดเศษ ถ้าเศษ >= 5 ปัดเลขขึ้น
    if x_neg_move_deci >= 5 :
        x_neg_move_deci = x_neg_without_deci + 1
    #เศษ < 5 ปัดลง
    else: x_neg_move_deci = x_neg_without_deci + 0
    #แสดงค่า แต่ต้อง *-1 เข้าไปเพราะจากขั้นตอนข้างบนตัวเลขจะเป็นค่าบวก แต่เราต้องการคำตอบที่เป็นค่าลบ 
    return int(x_neg_move_deci)*-1  

if __name__ == '__main__':
    main()