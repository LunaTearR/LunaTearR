#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 11
# Problem 2
# 204111 Sec 002

def main():
    list_x = [("11/1/1900", "Event A"), ("11/1/1900", "Event A"),
 ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
 ("9/3/2013", "Event E")]

    key = '09/03/2013'
    event = search_event(list_x, key)
    print("---")
    print(event)

def  search_event(list_x, key):
    newkey = []
    newkey.append(key.split("/")) #Remove slash from list.
        
    single_list = sum(newkey, []) #Turn to single list.

    day = single_list[0]
    day_separate = list(str(day)) #separate list day into two elements.

    month = single_list[1]
    month_separate = list(str(month)) #separate list month into two elements.

    if day_separate[0] == '0':  
        del_zero_day = (single_list[0].split("0"))
        del_zero_day.pop(0) #Remove 0 from list.
        turn2str = " "
        str_day = turn2str.join(del_zero_day)
        single_list[0] = str_day    #Chang day (zero),(digit) to (zero)(digit)
        key = str(single_list[0])+ '/' + str(single_list[1]) + '/' + str(single_list[2]) #Add slash to string.
    else:
        key = key

    if month_separate[0] == '0': 
        del_zero_month= (single_list[1].split("0"))
        del_zero_month.pop(0) #Remove 0 from list.
        turn2str = " "
        str_month = turn2str.join(del_zero_month)
        single_list[1] = str_month  #Chang month (zero),(digit) to (zero)(digit)
        key = str(single_list[0])+ '/' + str(single_list[1]) + '/' + str(single_list[2]) #Add slash to string.
    else:
        key = key


    event = dict(list_x) #Make list into dictionary.
    if key in event:
        event_is = (event[key])
        output = (key, event_is)
        return output
    else:
        return None
if __name__ == '__main__':
    main()