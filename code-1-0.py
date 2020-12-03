# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:37:15 2020

@author: micah

advent of code 2020
"""


file_name = "day1.txt"
f = open(file_name, "r")
expenses = f.read().split()
print(expenses)
def search_pairs():
    for item in expenses:
        for addend in expenses:
            if int(addend)+int(item) == 2020:
                return int(addend)*int(item)
            
      
def search_threes():
    for one in expenses:
        for two in expenses:
            for three in expenses:
                if int(one) + int(two) + int(three) == 2020:
                    return int(one) * int(two) * int(three)
        
print(search_pairs())
print(search_threes())