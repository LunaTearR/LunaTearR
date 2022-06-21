#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 02
# Problem 4
# 204111 Sec 002

#1  day = 24 hrs
#24 hrs = 1440 minutes
#1  hr  = 60 minutes
#60 mins = 3600 sec
#1 min = 60 sec
#1 min /60 sec = 60,000 milisec
#1 sec = 1000 millisec
#24 hrs = 86,400 seconds
#24 hrs = 86,400,000 milliseconds
#1 hrs = 3,600,000 milisec

# // = หารไม่เอาเศษ
#  % = modulo; เอาค่าเศษ

x = int(input("Input number of milliseconds: ")) #input number of milliseconds that you want to covert to days,hrs,mins,secs,and millsec.
day1 = (x//86400000)	#ไม่เอาเศษ
day2 = (x%86400000)		#เอาเศษที่เหลือจากการคิดก่อนหน้านี้ไปคิดเป็นค่าต่อๆไป (hrs, mins, secs, milis)
hr1 = (day2//3600000)
hr2 = (day2%3600000)
m1 = (hr2//60000)
m2 = (hr2%60000)
s1 = (m2//1000)
s2 = (m2%1000)
mi1 = s2

print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s) " %(day1,hr1,m1,s1,mi1))