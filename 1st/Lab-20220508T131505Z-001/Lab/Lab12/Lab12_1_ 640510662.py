#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 12
# Problem 1
# 204111 Sec 002

def main():
	x=int(input())
	y=int(input())
	print(gcd(x,y))
def gcd(x, y):
	if (y==0):
		return x
	else:
		return gcd(y,x%y)

if __name__ == '__main__':
	main()