#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 08
# Problem 3
# 204111 Sec 002

def main():

    nums = [1,2,3,4]
    n = 1
    #print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))   #[4, 1, 2, 3]

    n = 105
    #print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[4, 1, 2, 3]

    n = -1
    #print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[2, 3, 4, 1]

def nondest_rotate_list(list_a, n):
    for i in range(abs(n)):                     #Do this loop for 'n' times.
        if n > 0:                               #If 'n' is positive integer, rotate numbers in list to the right.
            new_list = list_a[-1:]+list_a[:-1]  #Remove the last number from list, then add it to the first position of list.
            list_a = new_list                   #Change last list to the new list.
            
        elif n < 0 :                         #If 'n' is negative integer, rotate numbers in list to the left.
            new_list = list_a[1:]+list_a[:1] #Remove the first number form list, then add it to the last position of list.
            list_a = new_list                #Change last list to the new list.
            
    return list_a

if __name__ == '__main__':
    main()