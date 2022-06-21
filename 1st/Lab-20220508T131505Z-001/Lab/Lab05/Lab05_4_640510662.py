#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 05
# Problem 4
# 204111 Sec 002


def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    '''
    l1+w1<l2
    เทียบจุด ขวาสุดของ4เหลี่ยมรูปแรก กับ ซ้ายสุดของ4เหลี่ยมรูปสอง
    หรือ
    l2+w2<l1 
    เทียบจุด ขวาสุดของ4เหลี่ยมรูปสอง กับ ซ้ายสุดของ4เหลี่ยมรูปแรก
    
    t1+h1<t2
    เทียบจุด ล่างสุดของ4เหลี่ยมรูปแรก กับ บนสุดของ4เหลี่ยมรูปสอง
    t2+h2<t1
    เทียบจุด บนสุดของ4เหลี่ยมรูปสอง กับ ล่างสุดของ4เหลี่ยมรูปแรก
    '''
    if (l1+w1<l2 or l2+w2<l1 or t1+h1<t2 or t2+h2<t1):
        over_lapped = False
    else:
        over_lapped = True
    return over_lapped

def main():
    l1 = int(input())
    t1 = int(input())
    w1 = int(input())
    h1 = int(input())
    l2 = int(input())
    t2 = int(input())
    w2 = int(input())
    h2 = int(input())
    print(is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2))


if __name__ == '__main__':
    main()
