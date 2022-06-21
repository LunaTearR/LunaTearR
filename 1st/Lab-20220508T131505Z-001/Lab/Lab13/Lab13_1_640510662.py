#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 13
# Problem 1
# 204111 Sec 002

def main():
    list_x =[[2, 3, 4],
[1, 2, 3]]
    
    print(square_matrix(list_x))
    print(list_x)
def square_matrix(list_x):
    len_row = len(list_x)
    len_col =len(max(list_x, key=len))
    max_len = max(len_row, len_col) #Compare lenses and columns which is greatest.

    #Create a list of zero by the possible maximum number of lenses and columns.
    result =  [[0 for row in range(max_len)] 
					for col in range(max_len)] 
    
    #Loop for append list_x into list of zero
    for i in range(len(list_x)):
        for j in range(len(list_x[i])):
            
            result[i][j] += list_x[i][j]

    #Destructive list_x
    #loop for delete elements in list_x
    for i in range(len(list_x)):
        del list_x[0]
    #loop for replace elements from list result into list_x
    for i in range(len(result)):
        list_x.append(result[i])
    #return list_x

if __name__ == '__main__':
    main()
	