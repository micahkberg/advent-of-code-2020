# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 08:22:33 2020

@author: micah

advent of code 2020 12.9.2020
"""

filename = "day9.txt"
f = open(filename, 'r')
nums = f.read().split()
nums = list(map(int,nums))

#find the invalid number iterating through each 25 number segment...
for i in range(25,len(nums)):
    valid = False
    for j in range(0,24):
        if valid == True:
            break
        for k in range(j+1,25):
            if nums[i-25+j] + nums[i-25+k] == nums[i]:
                valid = True
                break
    if valid == False:
        invalid_num = nums[i]
        print(invalid_num)
        break
    
#now iterate through all possible contiguous sums, can breka once the sum is too big
for i in range(0,len(nums)):
    solution_found = False
    for j in range(1,len(nums)-i):
        if sum(nums[i:i+j+1])==invalid_num:
            solution_found = True
            solution_num_list = nums[i:i+j+1]
            solution_num_list.sort()
            #print(solution_num_list)
            break
        elif sum(nums[i:i+j+1]) > invalid_num:
            break
    if solution_found == True:
        break
    
#sort and sum first and last numbers    
print(solution_num_list[0]+solution_num_list[-1])
