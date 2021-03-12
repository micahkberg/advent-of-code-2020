# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 2020

@author: micah

advent of code 12/19/2020
"""

import re

filename = "day19.txt"
f = open(filename, 'r')
rules_text,messages_text = f.read().split("\n\n")
rules_text = rules_text.split("\n")
messages =messages_text.split("\n")

def construct_rules_dict(rules_arr):
    output_dic = {}
    for rule in rules_arr:
        key,val = rule.split(":")
        val = val.strip(" ").replace('"','')
        if "|" in val:
            val = "(" + val + ")"
        output_dic[key] = val
    return output_dic

rules = construct_rules_dict(rules_text)

          
    


def make_rules_regex(dic):
    rule = rules['0']
    
    while any(char.isdigit() for char in rule):
        
        try:
            i, key = next((i,num) for (i,num) in enumerate(rule) if num.isdigit() and rule[i+1] != "}")
            if i+1 != len(rule):
                for N in rule[i+1:]:
                    if N.isdigit():
                        key+=N
                    else:
                        break
                     
        
            rule = rule[0:i]+  rules[key] + rule[i+len(key):]
        except:
            print("hit end of string probably")
            break
            
    return("^"+rule.replace(" ","")+"$")

reg_ex_rule = make_rules_regex(rules)

def get_matches(regexp):
    count = 0
    for line in messages:
        if re.search(regexp,line):
            count+=1
    return count
print("Part 1")
print(get_matches(reg_ex_rule))


#fixing for part 2
#rules["8"] = "(42 | 42 8)" - > but this goes infinite, so need to alter this to regex
rules["8"] = "(42)+"

#rules["11"] = "(42 31 | 42 11 31)"... oh no i dont know how to capture a matched group and then figure out how long it was......
rules["11"]  = "((42 31)|((42){2} (31){2})|((42){3} (31){3})|((42){4} (31){4})|((42){5} (31){5})|((42){6} (31){6})|((42){7} (31){7})|((42){8} (31){8})|((42){9} (31){9}))"

new_regex= make_rules_regex(rules)

print("part 2")
print(get_matches(new_regex))





