#!/usr/bin/env python3
# นายธีรภัทร์ นิลศิริ
# 640510662
# Lab 05
# Problem 5
# 204111 Sec 002

def zodiac_element(year):
    e = str(find_element(year)) + str(find_zodiac(year))
    return e  
    #ใช้Chinese calendarในการเทียบ

#เอาเลขลงท้ายมา % 10 เพื่อหาเลขหลักท้ายของปีแล้วเอาไปเทียบกับเลขลงท้ายของปี
def find_element(year):
    element = year%10 
    if element == 0 or element == 1:
        return 'Metal ' 
    elif element == 2 or element == 3:
        return 'Water '
    elif element == 4 or element == 5:
        return 'Wood '
    elif element == 6 or element == 7:
        return 'Fire '
    else: # 8 or 9
        return 'Earth '

#เอาปีไป % ด้วยจำนวนปีนักษัตร แล้วเอาไปเทียบกับเลขลงท้ายของปี
def find_zodiac(year):
    zodiac = year%12 
    if zodiac == 0:
        return 'Monkey'
    elif zodiac == 1:
        return 'Rooster'
    elif zodiac == 2:
        return 'Dog'
    elif zodiac == 3:
        return 'Pig'
    elif zodiac == 4:
        return 'Rat'
    elif zodiac == 5:
        return 'Ox'
    elif zodiac == 6:
        return 'Tiger'
    elif zodiac == 7:
        return 'Rabbit'
    elif zodiac == 8:
        return 'Dragon'
    elif zodiac == 9:
        return 'Snake'
    elif zodiac == 10:
        return 'Horse'
    else: #zodiac == 11
        return 'Goat'

def main():
    year = int(input())
    print(zodiac_element(year))

if __name__ == '__main__':
    main()
