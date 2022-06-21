#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 06
# Problem 4
# 204111 Sec 002

def main():
    # ด้านล่างเป็นแค่โครงสำหรับการแสดงผล นักศึกษาสามารถเขียนเพิ่มหรือแก้ไขตามความเหมาะสม
    total = int(input("Total students: "))
    print('Enter score:')
    
    total_count = total
    score_count = 0 
    total_score = 0 
    score = 0 
    highest = score
    runner_up = 0

    while score_count < total_count: #    
        score = float(input()) 

        if score < 0 : 
            continue

        total_score = total_score + score #เอาค่าscore มารวมกันเรื่อยๆจนครบตามที่ใส่ไป
        score_count = score_count + 1 #นับจำนวนครั้งที่ใส่ค่า score ทำจนกว่าจะเท่ากับค่า total student
           
        if ( score > highest): #ค่า score เปลี่ยนทุกครั้งที่ inputเข้ามาใหม่ และเอาไปเทียบกับ score (highest) ก่อนหน้า
            runner_up = highest #ค่าที่รองจากค่า highest
            highest = score #ค่า highest
        elif (score > runner_up and score < highest) : 
            runner_up = score
          
    print('---')
    print('Max score is: {0:.2f}'.format(highest))
    if runner_up == 0 :
        print('Runner up is: None')
    else:
        print('Runner up is: {0:.2f}'.format(runner_up))
    print('Average is: {0:.2f}'.format(total_score / score_count))

if __name__ == '__main__':
    main()

  