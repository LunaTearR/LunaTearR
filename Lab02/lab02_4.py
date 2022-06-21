#lab02
#04

milli = int(input("Input number of milliseconds : "))
day = milli // 86400000
left = milli % 86400000
hour = left // 3600000
left = left % 3600000
minute = left // 60000
left = left % 60000
second = left // 1000
milli = left % 1000

print("Result = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)"%(day,hour,minute,second,milli))