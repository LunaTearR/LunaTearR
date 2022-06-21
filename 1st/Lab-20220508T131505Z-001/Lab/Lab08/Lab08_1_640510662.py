#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 08
# Problem 1
# 204111 Sec 002

import string

def main():
    print(is_anagram('I am Lord Voldemort!!!', 'Tom Marvolo Riddle'))

def is_anagram(str1, str2):

    #Turn string into lower case.
    turn_lower1 = str1.lower() 
    turn_lower2 = str2.lower()

    #Remove all puntuation from string.
    del_punct1 = turn_lower1.translate(str.maketrans('', '', string.punctuation))    
    del_punct2 = turn_lower2.translate(str.maketrans('', '', string.punctuation)) 

    #Remove all digits from string.
    del_digits1 = del_punct1.translate(str.maketrans('', '', string.digits))
    del_digits2 = del_punct2.translate(str.maketrans('', '', string.digits))

    #Remove space from string.
    del_space1 = del_digits1.replace(" ", "")    
    del_space2 = del_digits2.replace(" ", "")

    #Sorting string in list.
    sorting1 = sorted(del_space1)
    sorting2 = sorted(del_space2)
    
    if sorting1 == sorting2:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

