# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:22:37 2020

@author: micah

advent of code 12/11/2020
"""

import itertools

filename = "day11.txt"
f = open(filename, 'r')
seats = f.read().split()

"""
rule1 -> if a cell is empty and surrounded by empty, it gets filled
rule2 -> if a cell is full and surrounded by 4 full cells, it empties
rule3 -> otherwise nothing happens to a cell
"""


def get_neighbors(col,row,arr):
    dirs = list(itertools.product([-1,0,1],repeat=2))
    dirs.remove((0,0))
    count = 0
    for dir in dirs:
        neighbor = [row+dir[0],col+dir[1]]
        if 0<=neighbor[0]<len(arr) and 0<=neighbor[1]<len(arr[0]):
            if arr[neighbor[0]][neighbor[1]]=="#":
                count+=1
    return count


def get_sightline_neighbors(col,row,arr):
    dirs = list(itertools.product([-1,0,1],repeat=2))
    dirs.remove((0,0))
    count = 0
    for dir in dirs:
        neighbor = "."
        neighbor_loc = [row+dir[0],col+dir[1]]
        while neighbor == "." and 0<=(neighbor_loc[0])<(len(arr)) and 0<=neighbor_loc[1]<(len(arr[0])):
            neighbor = arr[neighbor_loc[0]][neighbor_loc[1]]
            neighbor_loc = [neighbor_loc[0]+dir[0],neighbor_loc[1]+dir[1]]
        if neighbor=="#":
            count+=1
    return count   

def calc_update_array_immediate_neighbors(arr):
    new_arr = []
    stable = True
    for row_num in range(len(arr)):
        new_row = ""
        for col_num in range(len(arr[0])):
            tile = arr[row_num][col_num]
            if tile == "#" and get_neighbors(col_num,row_num,arr)>=5:
                new_row += "L"
                stable = False
            elif tile == "L" and get_neighbors(col_num,row_num,arr)==0:
                new_row += "#"
                stable = False
            else:
                new_row += tile
        new_arr.append(new_row)
        
    return(new_arr,stable)

def calc_update_array_sightline_neighbors(arr):
    new_arr = []
    stable = True
    for row_num in range(len(arr)):
        new_row = ""
        for col_num in range(len(arr[0])):
            tile = arr[row_num][col_num]
            if tile == "#" and get_sightline_neighbors(col_num,row_num,arr)>=5:
                new_row += "L"
                stable = False
            elif tile == "L" and get_sightline_neighbors(col_num,row_num,arr)==0:
                new_row += "#"
                stable = False
            else:
                new_row += tile
        new_arr.append(new_row)
        
    return(new_arr,stable)

stable = False
while stable == False:
    seats,stable = calc_update_array_sightline_neighbors(seats)
    
count=0
for row in seats:
    count += row.count("#")
print(count)    
                