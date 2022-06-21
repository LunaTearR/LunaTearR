#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 2
# 204111 Sec 002

import math
def main():
    x = int(input("number: "))
    base = int(input("base: ") or '10')
    if base ==10:
        print(digit_count(x))
    else:
        print(digit_count(x,base))

def digit_count(x, base=10):
    
    x = abs(x)
    epsilon = 10**-6                         #The value of epsilon is 0.000001      
    log = math.log(x,base) 

    if (log*10)%10 == 0:                     #In some cases, the decimal value is equal to zero. We'll add it by 1.
        #print('case1')                     
        log += 1

    elif 1-(float(log)-int(log)) <= epsilon: #Subtract [float(log)-int(log)] by 1 to turn it into decimal then use it to compare with epsilon.
        #print('case2') 
        log = math.ceil(log)+1               #If it's less than or equal to epsilon then plus by 1.
    else:
        #print('case3')
        log = log                            #If it's more than the value of epsilon do nothing.

    return math.ceil(log)                    #Round the number upward to it nearest integer.



def test_digit_count():
    assert(digit_count(2187,3) == 8 )
    #ค่าของ log 2187 base 3 คือ 7.0 ถ้าทศนิยมเป็น0 ให้เอาไปบวกเพิ่มด้วย 1
    
    assert(digit_count(-177147,3) == 12)
    #กรณีที่เป็นเลขติดลบ จะเปลี่ยนเป็นค่าลบด้วย absolute
    #ค่าของ log -177147 base 3 คือ 11.0 ถ้าทศนิยมเป็น0 แต่อาจจะมีต่อท้ายเนื่องจากคอมพิวเตอร์คำนวณออกมา ให้เอาไปบวกเพิ่มด้วย 1
    
    assert(digit_count(1000,10) == 4)
    #ค่าของ log 1000 base 10 คือ 2.9999999999999996 และเมื่อเอาทศนิยมมาลบด้วย 1 จะได้ค่าคือ 0.000000000009 ซึ่งน้อยกว่า epsilon จึงบวกด้วย 1
    
    assert(digit_count(1000) == 4)
    #ค่าของ log 1000 ค่า base ที่ไม่ใส่จะเป็น 10 คือ 2.9999999999999996 และเมื่อเอาทศนิยมมาลบด้วย 1 จะได้ค่าคือ 0.000000000009 ซึ่งน้อยกว่า epsilon จึงบวกด้วย 1
    
    assert(digit_count(4141,10) == 4)
    #ค่าของ log 4141 base 120 คือ 11 ซึ่งไม่มีเศษให้ตรวจสอบให้ return 11 ออกมาเลย 

    print ('Its TRUE no need to DEBUG it.')


if __name__ == '__main__':
    main()
    test_digit_count()




