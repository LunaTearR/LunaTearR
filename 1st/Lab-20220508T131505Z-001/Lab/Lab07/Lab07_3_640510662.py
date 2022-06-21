#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 1
# 204111 Sec 002

def main():
    n = int(input())
    triangle(n)

def triangle(n): #col = colume
    for row in range(n): 
        for col in range(row+1):    #row + 1 because loop function ends before it reach 'n' 
            
            if col==0 and col!=row and row!=(n-1): #print * vertically.
                print("*",end=".")
                '''
                When col is equal to 0 print  * with '.' vertically
                When col isn't equal to row do not print '.' when col and row equal to 0 
                When row isn't equal to (n-1), we won't print '.' at the last row behide the first *
                '''
            elif row==(n-1):        #print * at the last row horizontally.                    
                print("*",end=" ")
            elif row == col:        #print * at the end of the row.
                print("*",end='')
            elif row != col:        #print '.' in the empty space.
                print(".",end=".")
            else:
                pass
   
        print('')

if __name__ == '__main__':
    main()