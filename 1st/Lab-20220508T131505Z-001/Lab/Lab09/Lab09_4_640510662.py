#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 09
# Problem 4
# 204111 Sec 002
def main():
    list_a = [61, [[2, [75]], 8000, [39]], [58, [46]]] 

    print (sum_nested_list(list_a))

def sum_nested_list(list_a):
    
    sum_list = 0
    
    for i in list_a:
        if isinstance(i,list):  #Check at position i is list or not.
        						#If the element is a list turn it into list_a. If it's a single element, add it in to sum_list.
            sum_list += sum_nested_list(i) #Change the list to the list in side the list 
        else:					#If at position i is a single element and not a list, add it in to sum_list. 
            sum_list += i

    return sum_list


if __name__ == '__main__':
    main()