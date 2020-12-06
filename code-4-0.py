# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:23:57 2020

@author: micah

advent of code
"""

filename = "day4.txt"
f = open(filename, 'r')
lines = f.read().split('\n')

def make_passports():
    dicts = []
    current_dict = {}
    
    for line in lines:
        if line == '':
            dicts.append(current_dict)
            current_dict = {}
        else:
            items = line.split(" ")
            for item in items:
                key, value = item.split(":")
                current_dict[key] = value
                
    return dicts

def is_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def between(minm,val,maxm):
    return minm <= val <= maxm


def byr(val):
    try:
        return between(1920,int(val),2002)
    except:
        return False
    
def iyr(val):
    try:
        return between(2010,int(val),2020)
    except:
        return False
    
def eyr(val):
    try:
        return between(2020,int(val),2030)
    except:
        return False
    
def hgt(val):
    try:
        unit = val[-2:]
        height = int(val[:-2])
        if unit == "cm" and 150 <= height <= 193:
            return True
        elif unit == "in" and 59 <= height <= 76:
            return True
        else:
            return False
    except:
        return False
    
def hcl(val):
    if val[0] == "#":
        try:
            hexa = int(val[1:] , 16)
            if len(val[1:]) == 6:
                return True
            else:
                return False
        except:
            return False
    
def ecl(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(val):
    return len(val)==9
            

def check_passports():
    field_names = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    
    fields = [byr,iyr,eyr,hgt,hcl,ecl,pid]
    
    valid_count = 0
    for passport in passport_list:
        valid = True
        i = 0
        for field in field_names:
            if field not in passport.keys():
                valid = False
                print("missing key:" + field)
                break
            if not fields[i](passport[field]):
                print("Invalid field: " + passport[field])
                valid = False
                break
            
            i+=1
            
        if valid==True:
            valid_count += 1
    return(valid_count)


passport_list = make_passports()
print(check_passports())

