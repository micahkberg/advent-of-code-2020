# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:19:57 2020

@author: micah

advent of code 12/5/2020
"""

filename = "day5.txt"
f = open(filename, 'r')
passports = f.read().split('\n')[0:-1]


def get_bin(string):
    if "B" in string or "F" in string:
        nums = {"F": 0, "B": 1}
    else:
        nums = {"R": 1, "L": 0}
        
    bin_val = 0
    init_val = 2**(len(string)-1)
    for i in string:
        bin_val += nums[i]*init_val
        init_val = init_val/2
    return bin_val            
    
    
def make_passport_info():
    data = []
    biggest_id = -10
    for passport in passports:
        row = get_bin(passport[0:7])
        col = get_bin(passport[-3:])
        seat_id = (8 * row) + col
        if seat_id > biggest_id:
            biggest_id = seat_id
        data.append([row,col,seat_id])
            
    print("largest id number: " + str(biggest_id))
    return data
    
def search_for_missing_seat(): 
    data = make_passport_info()
    data.sort()
    last_seat_num = data[0][1] - 1
    last_line = data[0]
    for line in data:
        if line[1] != (last_seat_num+1)%8:
            print("my seat")
            print(last_line)
            break
        last_seat_num = line[1]
        last_line = line
    
search_for_missing_seat()
        