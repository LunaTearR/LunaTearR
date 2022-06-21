#!/usr/bin/env python3
# นายธีรภัทร์ นิลศิริ
# 640510662
# Lab 04
# Problem 1
# 204111 Sec 002

def love6(first, second):
    #each of them is 6
    if first == 6 or second == 6 :
        return True
    #sum of two is 6
    elif (first+second) == 6 :
        return True
    #diff of two is 6
    elif abs(first-second) == 6 :
        return True
    else:
        return False

def main():
    # receive input from user
    first = int(input())
    second = int(input())
    # print result from function
    print(love6(first,second))

if __name__ == '__main__':
    main()
