#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 08
# Problem 4
# 204111 Sec 002

def main():
#===========================================#
    #print("TEST 1")
    n = 1
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]

 #===========================================#
    #print("TEST 2")
    n = -2
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[2, 3, 4, 1]

 #===========================================#
    #print("TEST 3")   
    n = 105
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]
#===========================================#

def dest_rotate_list(list_a, n):
    for i in range(abs(n)):
        if n > 0:                       #If 'n' is positive integer, rotate numbers in list to the right.
            pop_out = list_a.pop()      #Remove the last number from list.
            list_a.insert(0,pop_out)    #Insert the number that has been removed to the first position of list.
           
        elif n < 0:                     #If 'n' is negative integer, rotate numbers in list to the left.
            pop_out = list_a.pop(0)     #Remove the first number from list.
            list_a.extend([pop_out])    #Insert the number that has been removed to the last position of list.
           
    return None

if __name__ == '__main__':
    main()