#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 11
# Problem 5
# 204111 Sec 002

def main():
    
    num1 = int(input())
    num2 = int(input())
    print(prime_factor(num1))
    print(prime_factor(num2))
    print(coprime_factor(num1, num2))
    #print("-----")
    '''
    print(prime_factor(180))
    print(prime_factor(48))
    print(coprime_factor(180, 48))
    print("-----") 
    print(prime_factor(164115 ))
    print(prime_factor(1406700))
    print(coprime_factor(164115 , 1406700))
    print("-----")
    print(prime_factor(438617401))
    print(prime_factor(8468460))
    print(coprime_factor(438617401, 8468460))
    print("-----")
    print(prime_factor(9978320))
    print(prime_factor(62244))
    print(coprime_factor(9978320, 62244))
    print("-----")
    print(prime_factor(30315475))
    print(prime_factor(24440870))
    print(coprime_factor(30315475, 24440870))
    print("-----")
    print(prime_factor(33554432))
    print(prime_factor(33554432))
    print(coprime_factor(33554432, 33554432))
    print("-----")
    print(prime_factor(62244))
    print(prime_factor(9978320))
    print(coprime_factor(62244, 9978320))
    print("-----")
    '''

def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

    '''
    num_ = n
    i = 2
    factors = []
    while ((n**0.5)>=i):
        if n%i == 0:
            n = n // i
            factors += [i]        
        else:
            i += 1
    if n == 0 or n == 1: 
        factors += []
        return factors
    elif (n == num_):
        factors += [n] 
        return factors
    else:
        factors += [n]
        return factors
    '''
    
def coprime_factor(a, b):
    num1 = (prime_factor(a))
    #print(num1)
    num2 = (prime_factor(b))
    #print(num2)
    co_prime = []
    if len(num1)<len(num2):
        for num in num1:
            if num in num2 :
                co_prime.append(num)
                #num1.remove(num)  
                num2.remove(num) 

    else:
        for num in num2:
            if num in num1 :
                co_prime.append(num) 
                #num2.remove(num)
                num1.remove(num)

    return co_prime

if __name__ == '__main__':
    main()