#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 09
# Problem 5
# 204111 Sec 002

def main():
    p = [(4, 1), (3, -1), (2, -1), (1, -1), (0, -1)]

    x = 'x'
    print(print_polynomial(p, x ))

def print_polynomial(p, x):
   
    p = list(reversed(sorted(p))) # [(2,-6), (1, 34), (0, -8)],x | -6x^2 + 34X -8
    
    for i in p:
        for j in p:
            if j[1] == 0:
                p.remove(j)
    
    first = True
    result = []
    for item in p:
        cof = item[1]
        if first:
            if cof > 0 : sign = ""
            else: sign = "-"
            first = False

        else:
            
            if cof > 0:
                sign = " + "
            else: sign = " - "
        

        power = (item[0])

        if abs(cof) == 1: #Coefficient is 1
            if power == 1:
                result.append("{0}{1}".format(sign,x))
            elif power == 0:
                result.append("{0}{1}".format(sign,abs(cof)))
            else:
                result.append("{0}{1}^{2}".format(sign,x,power))

        elif power > 1 : #Power more than 1
            result.append("{0}{1}{2}^{3}".format(sign,abs(cof),x,power)) 

        elif power == 1: #Power is 1
            result.append("{0}{1}{2}".format(sign,abs(cof),x))
        
        else:
            result.append("{0}{1}".format(sign,abs(cof)))

    
    return "".join(result)
if __name__ == '__main__':
    main()