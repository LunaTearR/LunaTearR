#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 02
# Problem 3
# 204111 Sec 002

print("First Equation")
m1 = float(input("Input m1: ")) #m = slop
b1 = float(input("Input b1: ")) #b = constant
print("Second Equation")
m2 = float(input("Input m2: "))
b2 = float(input("Input b2: "))
x = -((b1-b2)/(m1-m2)) 	#สูตรการหาค่า X
y = (m1*x)+b1			#สูตรการหาค่า Y
print("The point of intersection is at x = %.2f and y = %.2f " %(x,y))