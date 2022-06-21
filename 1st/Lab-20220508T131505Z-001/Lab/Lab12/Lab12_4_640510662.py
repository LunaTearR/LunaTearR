#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 12
# Problem 4
# 204111 Sec 002

def series(n):
    if n <= 1:
        return n
    else:
        if(n%2 == 0):
            return((series(n-1)*2) + 1)
        else:
            return((series(n-1)*2) - 1)
        

def main():
    x = int(input(""))
    print(series(x))
if __name__ == '__main__':
    main()