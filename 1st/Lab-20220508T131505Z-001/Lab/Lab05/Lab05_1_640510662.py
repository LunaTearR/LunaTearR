#!/usr/bin/env python3
# นายธีรภัทร์ นิลศิริ
# 640510662
# Lab 05
# Problem 1
# 204111 Sec 002

#-1 ห่างกัน
#0 ติดกัน
#1 ทับกัน
def eulcid_dis(x1, y1, x2, y2):
    return ((abs(x1-x2)**2 + abs(y1-y2)**2))**(1/2) #square root of (x1-x2)^2 + (y1-y2)^2
    
def intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6):
    d = eulcid_dis(x1, y1, x2, y2) #distance between 2 pointss
    y = abs(d-(r1+r2)) #distance of linear line between two circles.
    y0 = abs(d- (abs(r1 - r2 ))) # distance of linear line between two circle in case of have center point of one circle is in another circle.
    
    if d == (r1+r2) or (d == abs(r1 - r2)) or (y <= epsilon) : #two circle seperate but touch to each other.
        #print("touching") #touching
        result = 0

    #if circles is non-touching (-1) but tangent line is <= epsilon.
    elif d > (r1+r2): #two circles seperated
        if y<= epsilon:
            #print("touching2")
            result = 0
        else:
            #print("non-intersceting")
            result = -1 #non-intersceting

    #Intersection, touching, and non-touching&intersection. 
    elif d <(r1+r2) : #two circles is near to each other.
        if y0 <= epsilon: #read on some line that have y0.
            #print("39")
            result = 0 #touch
        elif d > abs(r1-r2): #one circle is larger than the other one and it intersect
            result = 1
        elif y0 > epsilon:
            #print("42")
            result = -1 #non-touching&intersection.
        elif (d==0) and ((r1>r2) or (r2>r1)): #when the centers of two circles are on the same point and one circle is larger than the other
            #print("45")
            result -1 #non-touching&intersection.
        elif (d==0) and (((r1/r2) == 1) or ((r2/r1 == 1))): #When the centers of two circles are at the same point and the two circles are the same size.
           #print("48")
            result = 0 #touch
        else: 
            pass


    else:
        result = 1
    return result

def main():
    # receive input from user
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    # print result from function
    print(intersects(x1, y1, r1, x2, y2, r2))

if __name__ == '__main__':
    main()



