# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 07:57:51 2020

@author: micah

advent of code 12/16/2020
"""

filename = "day16.txt"
f = open(filename, 'r')
tix_data = f.read().split("\n")

rules = {}
other_tix = []


my_ticket_next = False
ticket_data_next = False


for line in tix_data:
    if " or " in line:
        field_name = line.split(":")[0]
        ranges = [line.split(" ")[-3].split("-"),line.split(" ")[-1].split("-")]
        rules[field_name] = ranges
    elif line == "your ticket:":
        my_ticket_next = True
    elif my_ticket_next:
        my_ticket = line
        my_ticket_next = False
    elif line == "nearby tickets:":
        ticket_data_next = True
    elif ticket_data_next and line != "":
        other_tix.append(line.split(","))


def check(field_value,rule_matrix):
    if int(rule_matrix[0][0]) <= field_value <= int(rule_matrix[0][1]) or int(rule_matrix[1][0]) <= field_value <= int(rule_matrix[1][1]):
        return True
    else:
        return False

    
bad_values = []
bad_tix_id = []
ok_tix = []
for tix in other_tix:
    tix_ok = True
    for field in tix:
        field_ok = False
        for rule in rules.values():
            if check(int(field),rule):
                field_ok = True
        if not field_ok:
            bad_values.append(int(field))
            bad_tix_id.append(other_tix.index(tix))
            tix_ok = False
    if tix_ok:
        ok_tix.append(tix)
            
# solution to part 1
print(sum(bad_values))

solutions = {}


#go thru each slot in the ticket
for field_num in range(len(ok_tix[0])):
    #make a list of all the field names
    possible_field_names = list(rules.keys())
    #for each name
    for name in possible_field_names:
        name_ok = True
        #check the slots on the tickets to see if they fit the ranges
        for tix in ok_tix:
            if check(int(tix[field_num]),rules[name]):
                pass
            else:
                name_ok = False
                break
        if name_ok:
            try:
                solutions[field_num] = solutions[field_num] + [name]
            except:
                solutions[field_num] = [name]
#print(solutions)

solving = True
while solving:
    for key in list(solutions.keys()):
        if len(solutions[key])==1:
            for other_key in list(solutions.keys()):
                if key != other_key and solutions[key][0] in solutions[other_key]:
                    solutions[other_key].remove(solutions[key][0])
    
    solving = False
    for key in list(solutions.keys()):
        if len(solutions[key]) > 1:
            solving = True

print(solutions)
prod = 1
my_ticket = my_ticket.split(",")
for field_num in range(len(my_ticket)):
    if "departure" in solutions[field_num][0]:
        prod *= int(my_ticket[field_num])
        
print(prod)

                    