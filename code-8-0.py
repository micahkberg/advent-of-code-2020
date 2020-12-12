# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:07:15 2020

@author: micah

advent of code 2020 12/8/2020
"""
import copy

filename = "day8.txt"
f = open(filename, 'r')
lines = f.read().split("\n")[:-1]
original_program = []
for line in lines:
    original_program.append(line.split(" "))

## program data constructed
    


def run(program):
    accumulator = 0
    position = 0
    
    positions_visited = []
    
    while True:
        if position in positions_visited:
            print("infinite loop detected... resetting")
            return('infinite')
        elif position == len(program):
            return(accumulator)
        else:
            positions_visited.append(position)
        if program[position][0] == "acc":
            if program[position][1][0] == "+":
                accumulator += int(program[position][1][1:])
            else:
                accumulator -= int(program[position][1][1:])
            position += 1
        elif program[position][0] == "jmp":
            if program[position][1][0] == "+":
                position += int(program[position][1][1:])
            else:
                position -= int(program[position][1][1:])            
        elif program[position][0] == "nop":
            position += 1
            

for i in range(len(original_program)):
    new_program = copy.deepcopy(original_program)
    if original_program[i][0] == "jmp":
        new_program[i][0] = "nop"
    elif original_program[i][0] == "nop":
        new_program[i][0] = "jmp"
       
    if original_program[i][0] != "acc":        
        result = run(new_program)
        if result != "infinite":
            print("fix found")
            print(result)
            break
