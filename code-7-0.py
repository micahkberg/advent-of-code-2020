# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:53:42 2020

@author: micah

advent of code 2020 12/7/2020
"""


filename = "day7.txt"
f = open(filename, 'r')
rules = f.read().split("\n")

for i in range(len(rules)):
    rules[i] = rules[i].strip(".").split("contain")
    #print(rules[i][0])
    rules[i][0] = rules[i][0].replace(" bags ", "")
    if rules[i] == [""]:
        rules.remove(rules[i])
    #rules[i][1].split(",")
    #print(rules[i])
        
#print(rules)
    

def find_container(bag_type,containers):
    for rule in rules:
        try:
            if bag_type in rule[1] and rule[0] not in containers:
                containers.append(rule[0])
                containers = find_container(rule[0],containers)
        except:
            print("rule broken?")
            print(rule)
    return containers
    
print("potential external bag types")
print(len(find_container("shiny gold",[])))


def search_inside_bag(bag_type):
    bag_count = 0
    for rule in rules:
        if bag_type in rule[0]:
            rule_sub = rule[1].replace(" bags","").replace(" bag","").strip().split(", ")
            for part in rule_sub:
                if "no other" not in part:
                    bag_count += int(part[0])
                    bag_count += int(part[0])*search_inside_bag(part[2:])
                
    return bag_count


print(search_inside_bag('shiny gold'))
