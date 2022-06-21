#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 10
# Problem 5
# 204111 Sec 002
import string 
def main():
    code_table = (r'aceiklmr-')
    text = ('''
-3 
5 3 4 2 
3 1 2 8 1 7 2   0 86 ''')
    decode(code_table, text)

def decode(code_table, text):
    code_table = list(code_table)
    len_code = len(code_table)
    
    #For join adjacent numbers '1','2','3' => 123
    my_list = text.replace('\n', ' \n ')
    my_list = my_list.split(' ')
    
    print(my_list)    
    turn2str = ''
    for i in (my_list):
        if str.isnumeric(i):        #Check if elements in list is it number or not.
            if int(i) <= len_code:
                if int(i) == len_code :  #If value number in text is equal to value number of code_table (out of range) return '_'
                    i = '_'
                    turn2str += i
                else:                  #If value number is in len of code_table return string in the same value number of code_table
                    i = code_table[int(i)]
                    turn2str += i
            else:       #If value number of text us out of range code_table len return '_'
                i = '_' 
                turn2str += i
        elif i == ("\n"): #If it newline join it with above operation.
            turn2str += i 
        elif i in string.punctuation: #If it's punctuation do nothing.
            pass
        elif int(i) < 0 : #When number is negative return '_'
            i = '_'
            turn2str += i
        else:
            pass

    print (turn2str)
    

if __name__ == '__main__':
    main()