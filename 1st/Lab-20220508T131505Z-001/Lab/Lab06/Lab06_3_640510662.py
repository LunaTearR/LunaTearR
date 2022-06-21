#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 3
# 204111 Sec 002

def factorize(num): 
    #num / 2 ไปเรื่อยๆจนกว่าจะไม่ลงตัว
    num_ = num
    i = 2
    print (num , 'is ',end='')
    '''
    while num%2 == 0:
        #print เลข 2 ตามจำนวนครั้งสูงสุดที่หารได้
        print (2,end=' * ')
        num = num/2 
    '''
    #หลังจาก num / 2 ไม่ลงตัว(กลายเป็นเลขคี่) จึงเอา 3 มาหารต่อถ้าไม่ลงตัวก็ใช้ตัวถัดไปด้วย step = 2 ไปเรื่อยๆ
    #for i in range(3, int(math.sqrt(num))+1, 2):
    
    while ((num**0.5)>=i):
        if num%i == 0:
            num = num / i
            print (i,end=' * ')
        else:
            i += 1

    #ถ้า num เป็นจำนวนเฉพาะให้printค่าออกมาเลย
    if num == 0 or num == 1:
        print (int(num))
    elif (num == num_):
        print ('prime')
    else:
        print (int(num))
    
def main():
    num = int(input())
    factorize(num)

if __name__ == '__main__':
    main()
