#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 1
# 204111 Sec 002

def main():
    num = int(input("num: "))
    pos = int(input("pos: ")) 
    result = rotate(num, pos)
    print(type(result))
    print(result)

def rotate(num, pos):
    num1 = str(num)     #Turn number to string.
    for i in range(abs(pos)):
    #Determine the direction to move from value of pos.
        if pos>0:                                   #Rotate to the right when pos is positive value.
            num1 = list(num1)                       #Turn number to list.
            pop_out = num1.pop()                    #Remove the last number from list and keep it in 'pop_out'.      
            new_num = num1[:0]+[pop_out]+num1[0:]   #Add the number that has been removed from list to the 0 position.
            num1 = new_num                          #Change the list of numbers to the new list that has been edited.
                   
        elif pos<0:                         #Rotate to the left when pos is negative value.
            num1 = list(num1)               #Turn number to list.
            pop_out = num1.pop(0)           #Remove the first number in list.
            new_num = num1[:]+[pop_out]     #Add the number that has been removed to the last position of list
            num1 = new_num                  #Change the list of numbers to the new list that has been edited.
    
    #Final step change the list of numbers from above to integer.
    turn_to_int = "".join(num1)
    num1 = int(turn_to_int)  
    return  num1

if __name__ == '__main__':
    main()
