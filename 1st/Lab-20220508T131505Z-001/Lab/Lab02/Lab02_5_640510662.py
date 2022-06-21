#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 02
# Problem 5
# 204111 Sec 002

n = int(input("Enter n: ")) #input term that you want to know what value is it in fibonacci
a = (1+5**0.5)/2 			#fi #Golden Ratio
c = (a**n/(5**0.5)) + 0.5 	#fibonacci formula
print("fib(%.d) = %.d "%(n,c))
