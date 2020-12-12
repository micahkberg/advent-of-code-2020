# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:54:59 2020

@author: micah

advent of code 12/10/2020
"""

import itertools



filename = "day10.txt"
f = open(filename, 'r')
joltages = f.read().split()
joltages = list(map(int,joltages))
joltages.append(0)
joltages.sort()
joltages.append(joltages[-1]+3)
diffs = []

for i in range(1,len(joltages)):
    diffs.append(joltages[i]-joltages[i-1])
    
positions = [0]

reqs = []      
#get list of joltage adapters that are required
for jolt in joltages:
    if jolt == 0:
        reqs.append(jolt)
    elif jolt == joltages[-1]:
        reqs.append(jolt)
    elif (jolt+1 not in joltages and jolt+2 not in joltages) or (jolt-1 not in joltages and jolt-2 not in joltages):
        reqs.append(jolt)

total_permutations = 1


def check_diffs(lis,jump):
    for i in range(len(lis)-1):
        if lis[i+1]-lis[i]>3:
            return False
    try:
        if jump-lis[-1]>3:
            return False
    except:
        if jump>3:
            return False
    return True

for req in reqs[0:-1]:
    segment_permutations = 0
    jump = reqs[reqs.index(req)+1]-req
    adapters = []
    for j in range(1,jump):
        if req+j in joltages:
            adapters.append(j)
    adapters.sort()
    for j in range(0,len(adapters)+1):
        for arrangement in list(itertools.combinations(adapters,j)):
            if check_diffs(arrangement,jump):
                segment_permutations+=1
    total_permutations*=segment_permutations
    

print(total_permutations)