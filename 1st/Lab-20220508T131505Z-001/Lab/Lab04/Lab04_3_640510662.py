#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 04
# Problem 3
# 204111 Sec 002

def main():
    # receive input from user
    p = int(input( )) #จำนวน Pidgey
    c = int(input( )) #จำนวนลูกอม
    # print result from function
    print(calculate_p2p_evolve_exp(p, c))

def calculate_p2p_evolve_exp(p, c):
    pidgetto =  (p+c-1)//12 #หาจำนวนครั้งที่เป็นไปได้ที่จะสามารถ evolve ได้ #สามารถมอง p เป็น c ได้ #เป็นการรวบในการแลกนกเป็นลูกอมเข้าไปด้วย
    if p == 0 : #ไม่มี p จะไม่สามารถevolveได้ # -1 คือ กรณีที่ มี p=12 c=0 เอาไว้กันบัคที่จะออกมาคือได้ 500 exp  
        return 0 
    elif pidgetto >= p :    #ถ้าจำนวน p ที่เป็นไปได้(pidgetto)>= p ที่มี จำนวนครั้งที่แลกได้จะเท่ากับจำนวน p เพราะจะไม่สามารถแลกเกินจำนวนนกที่inputเข้าไปได้
        return p * 500
    else:  
        print('case2')                 #p > pidgetto #ถ้าจำนวน p ที่เป็นไปได้(pidgetto)< p ที่มี จะเข้าหลักการเอานกไปแลกเป็นลูกอมเพื่อใช้ในการ evolve
        return pidgetto *500 #case p = 20 c = 0 เอา p ไปแลกแล้วเป็น c แล้วเอามา evolve

if __name__ == '__main__':
    main()           