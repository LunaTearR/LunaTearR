#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 08
# Problem 5
# 204111 Sec 002

def num_to_word(num):

    if num == 0 :
        return 'zero'

    elif num >= 1 and num < 20: # 1 - 19
        return three_digits_to_word(num)
    
    elif num >= 20 and num < 100: # 20 - 99
        return  three_digits_to_word(int(num % 100))

    elif num >= 100 and num < 1000: # 100 - 999
        return three_digits_to_word(num // 100) + " hundred " + three_digits_to_word(int(num % 100))

    elif num >= 1000 and num < 1000000: # 1,000 - 999,999
        return three_digits_to_word(num // 1000) + " thousand " + three_digits_to_word(int(num % 1000))

    elif num >= 1000000 and num < 1000000000: #1,000,000  - 999,999,999 
        return three_digits_to_word(num // 1000000) + " million " + three_digits_to_word(int(num % 1000000))

    elif num >= 1000000000 and num < 1000000000000: #1,000,000,000 - 999,999,999,999
        return three_digits_to_word(num // 1000000000)+ " billion " + three_digits_to_word(int(num % 1000000000))


#==========================================================================================================#
def three_digits_to_word(n):
    num_list = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    thousand = 1000
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000 

    if (n < 20):                    #ถ้าเลขน้อยกว่า 20 (0-19) ให้คืนค่าตามตำแหน่งเลขใน num_list
        return num_list[n]

    elif (n < 100):                   #ถ้าเลขน้อยกว่า 100 (20-99) 
        if n % 10 == 0:             #กรณีที่เลขตัวท้ายเป็น 0 ให้คืนค่าตามตำแหน่งเลขใน num_list เทียบจาก n
            return num_list[n]
        else:                       #กรณีที่เลขท้ายไม่เป็น 0 ให้แยกเลขหลักสิบกันหลักหน่วยออกมาจากกัน Ex. 21 => 20 และ 1
            return num_list[(n // 10) * 10] + '-' + num_list[n % 10]

    elif (n < thousand):              #ถ้าเลขน้อยกว่า 1,000 (100-999)
        if n % 100 == 0:            #กรณีที่เลขหลักสิบกับหลักหน่วยเป็นศูนย์ ให้คืนค่าหลักร้อยโดยการนำเลขในตำแหน่งหลักร้อยไปเทียบกับ num_list
            return num_list[n // 100] + ' hundred'
        else:                       #กรณีที่เลขหลักสิบกับหลักหน่วยไม่เท่ากับศูนย์ ให้คืนค่าหลักร้อยโดยการนำเลขในตำแหน่งหลักร้อยไปเทียบกับ num_list และ คืนค่าหลักสิบและหลักหน่วยโดยนำไปเทียบกับ num_list (ใช้ three_digits_to_word เพื่อนำขั้นตอนก่อนหน้ามาช่วยคิด)
            return num_list[n // 100] + ' hundred ' + three_digits_to_word(n % 100)

    elif (n < million):               #ถ้าเลขน้อยกว่า 1,000,000 (1,000-999,999)
        if n % thousand == 0:       #กรณีที่หลักแรกไม่เท่ากับศูนย์แต่หลักอื่นๆเป็นศูนย์ คืนค่าหลักแรกโดยนำไปเทียบกับ num_list (ใช้ three_digits_to_word เพื่อนำขั้นตอนก่อนหน้ามาช่วยคิด)
            return three_digits_to_word(n // thousand) + ' thousand'
        else:                       #กรณีที่หลักแรกไม่เท่ากับศูนย์ส่วนหลักอื่นเป็นเลขใดๆ คืนค่าหลักอื่นๆโดยใช้ three_digits_to_word เพื่อนำขั้นตอนก่อนหน้ามาช่วยคิด
            return three_digits_to_word(n // thousand) + ' thousand ' + three_digits_to_word(n % thousand)

    elif (n < billion):               #ถ้าเลขน้อยกว่า 1,000,000,000 (1,000,000 - 999,999,999)
        if (n % million) == 0: 
            return three_digits_to_word(n // million) + ' million'
        else: 
            return three_digits_to_word(n // million) + ' million ' + three_digits_to_word(n % million)

    elif (n < trillion):              #ถ้าเลขน้อยกว่า 1,000,000,000,000 (1,000,000,000 - 999,999,999,999)
        if (n % billion) == 0: 
            return three_digits_to_word(n // billion) + ' billion'
        else: 
            return three_digits_to_word(n // billion) + ' billion ' + three_digits_to_word(n % billion)

def main():
    x = int(input(""))
    print(num_to_word(x))
    print(num_to_word(1000000))
    print(num_to_word(200000000))
    print(num_to_word(9000000))
    print(num_to_word(1000000000))
    print(num_to_word(9000000000))
    print(num_to_word(10000000000))
    print(num_to_word(80000000000))
    print(num_to_word(700000000000))
    print(num_to_word(1489662012))

if __name__ == '__main__':
    main()
