# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:50:13 2020

@author: micah

advent of code 12/6/2020
"""

filename = "day6.txt"
f = open(filename, 'r')
answers = f.read().split("\n")


def make_groups():
    current_group = [0,""]
    answers_grouped = []
    for line in answers:
        if line == "":
            answers_grouped.append(current_group)
            current_group=[0,""]
        else:
            current_group[0] += 1
            current_group[1] += line
            
        
    return answers_grouped


grouped = make_groups()
def total_yeses():
    total = 0
    for group in grouped:
        num = len(set(group[1]))
        total += num
    print("how many categories had yeses")
    print(total)
            
def all_yeses():
    total = 0
    for group in grouped:
        for char in set(group[1]):
            if group[1].count(char)==group[0]:
                total+=1
    
    print("where everyone said yes")
    print(total)
    
total_yeses()
all_yeses()