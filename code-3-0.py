# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:51:30 2020

@author: micah

advent of code
"""

fname = "day3.txt"
f = open(fname, "r")
map_data = f.read().split("\n")
map_data = map_data
print("height")
print(len(map_data))
print("width")
print(len(map_data[0]))
for x in map_data:
    if x=="":
        map_data.remove(x)


def test(slope):
    
    height = len(map_data)
    y_pos = 0
    x_pos = 0
    tree_count = 0
    
    while y_pos<(height):
        #print(str((slope[1]*y_pos)%len(map_data[0]))+','+str(y_pos))
        try:
            if map_data[y_pos][x_pos]=='#':
                tree_count += 1
        except:
            print("ERROR")
            print(map_data[y_pos])
            print(x_pos)
            print("END ERROR")
        y_pos += slope[0]
        x_pos = (x_pos + slope[1])%len(map_data[0])
    return(tree_count)

slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
test_results = []
for slope in slopes:
    test_results.append([slope,test(slope)])
mult = 1
for result in test_results:
    print(result)
    mult *= result[1]
print(mult)