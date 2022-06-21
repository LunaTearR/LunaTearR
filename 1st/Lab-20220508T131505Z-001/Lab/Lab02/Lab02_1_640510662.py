#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 02
# Problem 1
# 204111 Sec 002

f = int(input("Input temperature in Fahrenheit: ")) #input Fahrenhient
c = (f-32)/1.8 #Conversion Formula from Fahreneient to Celsius
print("%.2f degree Fahrenheit is %.2f degree Celsius" % (f,c))