# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:07:21 2020

@author: micah

advent of code 12/13/2020
"""



filename = "day13.txt"
f = open(filename, 'r')
timestamp,businfo_raw = f.read().split()
timestamp = int(timestamp)
businfo = list(filter(lambda a: a != "x", businfo_raw.split(",")))

#PART 1
times = []
for i in businfo:
    wait = int(i)-timestamp%int(i)
    times.append([wait,int(i)])

times.sort()
##print(times)
##print(times[0][0]*times[0][1])



#PART 2
businfo_raw = businfo_raw.split(",")
count = 0
num = []
rem = []
for i in businfo_raw:
    #print(i+" leaves at t + "+ str(count))
    if i != "x":
        num.append(float(i))
        rem.append(count)
    count+=1

def dumb_search():
    searching = True
    i = 0
    while searching:
        searching = False
        timestamp = i * 17
        for i in range(1,len(num)):
            if num[i] - timestamp%num[i] != rem[i]:
                searching = True
                print(timestamp)
                break
        i+=1
    return(i)
    #this took forever



def gcd(a,b):
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

def power(x,y,m):
    if y==0:
        return 1
    p = power(x,y//2,m)%m
    p = (p * p) % m
    if y%2==0:
        return p
    else:
        return ((x*p)%m)

def modInv(a,m): 
    
    g = gcd(a,m)
    if (g != 1): 
        print("broke") 
    else: 
        return power(a, m - 2, m) 
    

#chinese remainder theorem only works for the num[i] - rem[i]?        
def chinese_remainder_theorem():
    prod = 1.0
    fix_rem = []
    for i in range(len(num)):
        fix_rem.append(num[i]-rem[i])
        prod *= num[i]
        
    pp = []
    inv = []
    for i in range(len(num)):
        pp.append(prod/num[i])
        inv.append(modInv(pp[i],num[i]))
    result = 0
    for i in range(len(num)):
        result+= fix_rem[i] * inv[i] * pp[i]
        
    
    return result%prod
#worked on everything except for the puzzle input lol
    

def prod(lis):
    prod = 1
    for i in lis:
        prod *= i
    return(prod)


#this is the sieve method i think, still seems to take a long time
def another_method():
    x = 0
    inc = 1
    factor = 1
    cap = prod(num)
    print("ceiling is at "+ str(cap))
    
    

    for i in range(len(num)-1):
        inc *= num[i] 
        while (x+rem[i+1])%num[i+1] != 0 and x<cap:
            x+=inc
            if x>factor:
                factor *= 2
                print(x)
        if x>cap:
            print("hit cap")
    print("nums : expected: actual remainders")
    for i in range(len(num)):
        print(str(num[i])+" : "+str(rem[i])+" : "+str(num[i]-(x%num[i])))
    
    return(x)
print(another_method())






        
#print(chinese_remainder_theorem())