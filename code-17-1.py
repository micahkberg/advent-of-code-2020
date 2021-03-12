# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:08:28 2020

@author: micah

advent of code 12/17/2020

part 2 (see 17-0 for part 1)

this one didn't run super fast, maybe there is a way to speed it up a bit...
"""

filename = "day17.txt"
f = open(filename, 'r')
flat_shape = f.read().split("\n")

# # -> active
# if active and 2-3 neighbors are active, remains active
# . -> inactive
# if inactive and 3 neighbors are active, gets activated

import itertools

#list of tuples that represent vectors to each neighbor from a given hypercube segment
neighbors = list(itertools.product([1,0,-1],repeat=4))
neighbors.remove((0,0,0,0))


initial_active_cubes = []

#make an initial array of activated cubes
for y in range(len(flat_shape)):
    for x in range(len(flat_shape[y])):
        if flat_shape[y][x] =="#":
            initial_active_cubes.append((x,y,0,0))

    
def get_neighbors(cube):
    neighbor_lis = []
    for neighbor in neighbors:    
        neighbor_lis.append((cube[0]+neighbor[0],cube[1]+neighbor[1],cube[2]+neighbor[2],cube[3]+neighbor[3]))

    return(neighbor_lis)


def cycle(active_cube_list):
    new_active_cubes = []
    neighborliness = {}
    
    
    for cube in active_cube_list:
        for neighbor in get_neighbors(cube):
            if neighbor in list(neighborliness.keys()):
                neighborliness[neighbor] += 1
            else:
                neighborliness[neighbor] = 1
    
    for cube in active_cube_list:
        if cube in list(neighborliness.keys()) and 2 <= neighborliness[cube] <= 3:
            new_active_cubes.append(cube)
            
    for cube in list(neighborliness.keys()):
        if cube not in active_cube_list and neighborliness[cube] == 3:
            new_active_cubes.append(cube)
            
    return new_active_cubes

def main():
    for i in range(6):
        print("Beginning Cycle "+ str(i))
        if i == 0:
            next_state = cycle(initial_active_cubes)
        else:
            next_state = cycle(next_state)
        
    print(len(next_state))
    
main()
            