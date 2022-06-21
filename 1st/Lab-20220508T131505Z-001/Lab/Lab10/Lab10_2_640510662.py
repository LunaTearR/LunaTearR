#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 10
# Problem 2
# 204111 Sec 002

def main():
	base_ten = int(input())
	trans2base = int(input())
	print(is_palindrome(base_ten, trans2base))

def is_palindrome(x, b):
	
	result = ''		#For join each number that has been modded
	while x != 0 :
		mod_num = x%b 	#Trans the number into the selected base by moduloe
		result += str(mod_num) #join each number that has been modded as string.
		x = x//b 	#Change the number by divide it by selected base.
	#print(result)
	trans_num=list(result) # Number that has been turned to new base from above operation.
	revse_num= list(reversed(trans_num)) #Reversed number.

	#===Another way===#
	'''
	while(int(result)!=0):  #Result is the number from above operation.
	    digit=int(result)%10 	#Keep the last digit of number.
	    revse_num=revse_num*10+digit  #Join the number.
	    result=int(result)//10 #Remove the last digit of number
	'''
	#=================#

	if(trans_num==revse_num):
	    return True
	else:
	    return False

if __name__=="__main__":
	main()