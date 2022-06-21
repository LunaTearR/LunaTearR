#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 11
# Problem 4
# 204111 Sec 002
# Help by ศุภกิตต์ อึ้ง (640510682)

import copy
def main():
    p1 = [(2, 0), (1, 0), (0, 0)]
    p2 = [(2, 0), (0, 0), (1, 0)]

    print(polynomial_addition(p1, p2))

def polynomial_addition(p1, p2):
    list1 = list(reversed(sorted(p1)))
    list2 = list(reversed(sorted(p2)))
    dict1 = dict(list1)
    dict2 = dict(list2)

    newlist1 = []
    for i in range(len(list1)):
        power = list1[i][0]
        newlist1.append(power)

    newlist2 = []
    for i in range(len(list2)):
        power = list2[i][0]
        newlist2.append(power)

    x = set(newlist1)
    y = set(newlist2)

    inter = list(x & y)
    notdup = list(x.union(y)-set(inter)) 
    #print(notdup)
    sum_poly = []
    
    for key in inter:
        if key in dict1 or dict2:
            sum_ = dict1[key] + dict2[key]
            sum_poly.append((key,sum_))
    #print(sum_poly)


    for key2 in notdup:
        if key2 in dict1:
            sum_poly.append((key2, dict1[key2]))
        elif key2 in dict2:
            sum_poly.append((key2, dict2[key2]))

    test = []
    clone = copy.deepcopy(sum_poly)
    for dup in (clone):
        if dup[1] == 0:
            sum_poly.remove(dup)
            test.append(dup)
    
    test2 = list(sum(test, ()))
    
    #print(test2.count(0))
    #print(clone)

    if test2.count(0) == len(clone):
        return []

    return list(reversed(sorted(sum_poly)))

if __name__ == '__main__':
    main()