#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 10
# Problem 4
# 204111 Sec 002

import string
def main ():
	str_line = 'cOdINg '
	print(uniform(str_line))

def uniform(line):
	upper_case = 0
	lower_case = 0
	first_chr = line[0] #Keep the first character of the string.
	for i in line:
		if i.isupper():    	#Check each characters in string is it upper case?
	 		upper_case += 1
		elif i.islower():	#Check each characters in string is it lower case?
	 		lower_case += 1 

	if upper_case == lower_case: #If number of upper and lower is equal.
		if first_chr.isupper():		#If first character is upper case. Turn all string to upper case.
			return(line.upper())
		elif first_chr.islower():	#If first character is lower case. Turn all string to upper case.
			return(line.lower())
	elif upper_case > lower_case:	#If number of upper more than lower.
		return(line.upper())		#Turn all string to upper case.
	elif upper_case < lower_case:	#If number of lower more than lower.
		return(line.lower())		#Turn all string to lower case.

if __name__ == '__main__':
	main()