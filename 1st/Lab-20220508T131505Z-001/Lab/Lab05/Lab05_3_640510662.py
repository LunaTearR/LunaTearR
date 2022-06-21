#!/usr/bin/env python3
# นายธีรภัทร์ นิลศิริ
# 640510662
# Lab 05
# Problem 3
# 204111 Sec 002

due_day = 13
due_month = 4

def find_leap_year(y): #check is that leap year or not
    y_leap_year = (y%4 == 0) and (y%100 != 0) or (y%400 == 0)
    return y_leap_year

def count_down_to_songkran(d, m, y):
    if m <= 4: #date b4 due_date
        if m==4 :
            if d <= 13:
                if find_leap_year(y) == False:
                    m = m-1
                    m0 = (month_to_date(m,y))
                    s_date = abs((d + (m0)))  #input date
                    due_date = abs((due_day +(90)))
                    output = abs(due_date - s_date)
                elif find_leap_year(y) == True:
                    m = m-1
                    m0 = (month_to_date(m,y))
                    s_date = abs(d + (m0))   #input date 365
                    due_date = abs((due_day +(91)))
                    output = abs(due_date - s_date) 
                else:
                    pass
                #print("case1")
                return output
            
            elif d>13: #date after due_date #still in april
                if find_leap_year(y) == True: #if next year is leap year
                    m = m-1
                    m0 = (month_to_date(m,y))
                    s_date = abs((d + (m0))-366)   #input date 
                    next_year = abs((due_day +(90))) 
                    output = (s_date + next_year)
                elif find_leap_year(y) == False:
                    y1 = y+1
                    if find_leap_year(y1) == False: 
                        m = m-1
                        m0 = (month_to_date(m,y))
                        s_date = abs((d + (m0))-365)   #input date 
                        next_year = abs((due_day +(90))) 
                        output = (s_date + next_year)
                    elif find_leap_year(y1) == True: 
                        m = m-1
                        m0 = (month_to_date(m,y))
                        s_date = abs((d + (m0))-365)   #input date 
                        next_year = abs((due_day +(91))) 
                        output = (s_date + next_year)

                #print("case2")
                return output
        elif m<4:
            if find_leap_year(y) == False:
                m = m-1
                m0 = (month_to_date(m,y))
                s_date = abs((d + (m0)))  #input date
                due_date = abs((due_day +(90)))
                output = abs(due_date - s_date)

            elif find_leap_year(y) == True:
                m = m-1
                m0 = (month_to_date(m,y))
                s_date = abs((d + (m0)))  #input date
                due_date = abs((due_day +(91)))
                output = abs(due_date - s_date) 
        return output        
        
    elif m > 4:
        if find_leap_year(y) == True: #if next year is leap year
            m = m-1
            m0 = (month_to_date(m,y))
            s_date = abs((d + (m0))-366)   #input date 
            next_year = abs((due_day +(90))) 
            output = (s_date + next_year)
        elif find_leap_year(y) == False:
            y1 = y+1
            if find_leap_year(y1) == False: 
                m = m-1
                m0 = (month_to_date(m,y))
                s_date = abs((d + (m0))-365)   #input date 
                next_year = abs((due_day +(90))) 
                output = (s_date + next_year)
            elif find_leap_year(y1) == True: 
                m = m-1
                m0 = (month_to_date(m,y))
                s_date = abs((d + (m0))-365)   #input date 
                next_year = abs((due_day +(91))) 
                output = (s_date + next_year)
        #print("case3")
        return output


def month_to_date(m,y): #days that have passed 
    if find_leap_year(y) == False:
        if m == 0:
            m_day = 0
        elif m == 1:
            m_day = 31  #1jan - 31jan
        elif m == 2:
            m_day = 59  #1jan - 28feb
        elif m == 3:    
            m_day = 90  #1jan - 31mar
        elif m == 4:
            m_day = 120 #1jan - 30apr
        elif m == 5:
            m_day = 151 #1jan - 31may
        elif m == 6: 
            m_day = 181 #1jan - 30jun
        elif m == 7:
            m_day = 212 #1jan - 31july
        elif m == 8:
            m_day = 243 #1jan - 31aug
        elif m == 9:
            m_day = 273 #1jan - 30sep
        elif m == 10:
            m_day = 304 #1jan - 31oct
        elif m == 11:
            m_day = 334 #1jan - 30nov
        elif m == 12:
            m_day = 365 #1jan - 31dec
    else:
        if m == 0:
            m_day = 0
        elif m == 1:
            m_day = 31  #1jan - 31jan
        elif m == 2:
            m_day = 60  #1jan - 29feb
        elif m == 3:    
            m_day = 91  #1jan - 31mar
        elif m == 4:
            m_day = 121 #1jan - 30apr
        elif m == 5:
            m_day = 152 #1jan - 31may
        elif m == 6: 
            m_day = 182 #1jan - 30jun
        elif m == 7:
            m_day = 213 #1jan - 31july
        elif m == 8:
            m_day = 244 #1jan - 31aug
        elif m == 9:
            m_day = 274 #1jan - 30sep
        elif m == 10:
            m_day = 305 #1jan - 31oct
        elif m == 11:
            m_day = 335 #1jan - 30nov
        elif m == 12:
            m_day = 366 #1jan - 31dec
    return m_day

def main():
    d = int(input())
    m = int(input())
    y = int(input())
    print(find_leap_year(y))
    print(count_down_to_songkran(d, m, y))

if __name__ == '__main__':
    main()