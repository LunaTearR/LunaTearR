#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 10
# Problem 5
# 204111 Sec 002

def main():
    message = (r"D and C")
    pattern = ('''
***************
******   ******
***************
''')

    (patterned_message(message, pattern))

def patterned_message(message, pattern):
    MessageDelSpcae = message.replace(" ", "") #Remove space in message
    ListMessage = list(MessageDelSpcae) #Turn massage into list.
    ListPattern = list(pattern) #Turn pattern into list.
    LenMessage = len(ListMessage)   #Check how many elements are in the list of message.
    OutPut = '' #For keep result
    Position = 0 #Let position start at 0

    for i in (ListPattern):
        if i == '*':
            if Position < LenMessage: #If position is in range of LenMessage
                i = ListMessage[Position]
                Position += 1 
                OutPut+= i
            else:   #If position is out of range of LenMessage
                Position = 0 #Let position start at 0
                i = ListMessage[Position]
                Position += 1 
                OutPut+= i
        else:
            OutPut+=i 

    print(OutPut)

if __name__ == '__main__':
    main()
