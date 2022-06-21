#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 11
# Problem 1
# 204111 Sec 002

def main ():
    list_x = ['11/1/2016', '2/1/201']
    #print(sort_date(list_date))
    print("---")
    print(sort_date(list_x))
    print(list_x)

def sort_date(list_x):
    newlist = []
    #====remove slash from list====#
    for i in range (len(list_x)):
        newlist.append(list_x[i].split("/"))
    
    #====Swap D/M/Y to Y/M/D====#
    for i in range (len(newlist)):
        newlist[i][0], newlist[i][2] = newlist[i][2], newlist[i][0]

    #====Combine list and change it into integer====#
    merge = []
    for i in range(len(newlist)):
        blank = []
        for j in range(len(newlist[0])):
            blank.append(int(newlist[i][j])) 
        merge.append(blank) 
    merge.sort() #Sorting date.
    
    #====Swap Y/M/D to D/M/Y====#
    for i in range(len(merge)):
        merge[i][0], merge[i][2] = merge[i][2], merge[i][0] 

    #====Add slash====#
    result =[]
    for i in range(len(merge)):
        n = str(merge[i][0])+ '/' + str(merge[i][1]) + '/' + str(merge[i][2])
        result += [n]

    #====Make it as destructive====#
    for i in range(len(result)):
        del list_x[0]
        list_x.append(result[i])

if __name__ == '__main__':
    main()
    