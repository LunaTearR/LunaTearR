#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 08
# Problem 2
# 204111 Sec 002

def classify(list_x):
    list_a = [] 
    list_b = [] 
    list_c = [] 
 #เขียนโค้ดลงไปตรงนี้
    for i in range(len(list_x)):
        remove = list_x.pop(0)  #Remove the first element in the list.
        type_ = (type(remove))  #The variable which keeps the element that has been removed.
        if type_ is int:                #If the element is class integer put it in list_a.
            list_a.append(remove)
        elif type_ is float:            #If the element is class float put it in list_b.
            list_b.append(remove)
        elif type_ is str:              ##If the element is class string put it in list_c.
            list_c.append(remove) 

#ในpython เราสามารถ return ได้มากกว่า 1 ค่า โดยผลลัพธ์จะถูกมัดรวมออกไปเป็นค่าเดียวซึ่งมี type เป็น  Tuple
    return list_a, list_b, list_c

def main():
    x = [10, 'he4>lo', 23.5, 4]
    list_int, list_float, list_string = classify(x)
    print(type(list_int), list_int)
    print(type(list_float), list_float)
    print(type(list_string), list_string)

#<class 'list'> [10, 4]
#<class 'list'> [23.5]
#<class 'list'> ['he4>lo']


if __name__ == '__main__':
    main()
