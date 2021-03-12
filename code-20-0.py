# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:28:58 2020

@author: micah

aoc 12/20/2020
"""

import itertools

filename = "day20.txt"
f = open(filename, 'r')
raw = f.read().split("\n\n")
camera_data = {}



def make_img_file(raw_tile):
    #print(raw_tile)
    n = raw_tile[0]
    s = raw_tile[-1]
    e = ""
    w = ""
    for line in raw_tile:
        e += line[-1]
        w += line[0]

    dic = {"n":n,
           "s":s,
           "w":w,
           "e":e,
           "tile":raw_tile}
    return dic

#makin a big dict with all the camera files in it.
for file in raw:
    file_lines = file.split("\n")
    if file_lines[1:] != []:
        camera_data[file_lines[0]] = make_img_file(file_lines[1:])
        
def check_match(tile1,tile2):   
    for i,j in list(itertools.product("news",repeat = 2)):
        if tile1[i] == tile2[j] or tile1[i] == tile2[j][::-1]:
            return True
    
    return False


def find_corners():
    corner_ids = []
    for tile1 in camera_data.keys():
        matches = 0
        for tile2 in camera_data.keys():
            if check_match(camera_data[tile1],camera_data[tile2]):
                matches+=1
        if matches == 2:
            corner_ids.append(tile1)
    return corner_ids
    
out = find_corners()
print(out)

