# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:12:07 2020

@author: micah

advent of code
"""

fname = "day2.txt"
f = open(fname, "r")
data = f.read().split("\n")

count= 0
for entry in data:
    #try:
    try:
        rule,letter,pw = entry.split(" ")
    except:
        print(entry)
    
    rule_min, rule_max = rule.split("-")
    letter = letter[0]
    letter_count = pw.count(letter)
    if letter_count <= int(rule_max) and letter_count >= int(rule_min):
        count+=1
    #except:
    #    print(entry)
print("old rule count")
print(count)
#print(len(data))

count= 0
for entry in data:
    #try:
    try:
        rule,letter,pw = entry.split(" ")
    except:
        print(entry)
    
    pos_1, pos_2 = rule.split("-")
    letter = letter[0]
    letter_count = pw.count(letter)
    if (pw[int(pos_1)-1]==letter) ^ (pw[int(pos_2)-1]==letter):
        count+=1

print("new rule count")
print(count)