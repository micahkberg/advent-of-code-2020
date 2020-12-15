# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:13:02 2020

@author: micah

advent of code 12/15/2020
"""

puzzle_input = [16,1,0,18,12,14,19]

def play_game(nums):
    while len(nums) < 2040:
        last_num = nums[-1]
        if last_num in nums[:-1]:
            nums.reverse()
            age = nums.index(last_num,1)
            nums.reverse()
            nums.append(age)
        else:
            nums.append(0)
            
    return(nums)

result = play_game(puzzle_input)
print(result[2020-1])



puzzle_input = [16,1,0,18,12,14,19]

def play_game_dict(nums):
    nums_dict = {}
    # said number : last turn it was said
    
    for i in nums[0:-1]:
        nums_dict[i] = nums.index(i)
    
    new_num = nums[-1]
    turn = len(nums)
    while turn < 30000002:
        if turn > 30000000-10:
            print("turn: "+ str(turn) + ", current number: " + str(new_num))
            
        
        
        if new_num in nums_dict.keys():
            
            age = turn - nums_dict[new_num] - 1
            nums_dict[new_num] = turn-1
            new_num = age
        else:
            nums_dict[new_num] = turn-1
            new_num = 0
           
        turn+=1
            
        if turn%1000000 ==0:
            print(str(turn/30000000.0 * 100.0) + "%")
            
    return(nums_dict)
    #return(list(nums_dict.keys())[list(nums_dict.values()).index(30000000-1)])

result_dic = play_game_dict(puzzle_input)

#wrong answers
#224129 (low)
#6698455 (low)
#9847000 ?
#16671510