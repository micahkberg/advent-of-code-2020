# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:07:21 2020

@author: micah

advent of code 12/11/2020
"""



filename = "day12.txt"
f = open(filename, 'r')
inputs = f.read().split()


dirs = {"N":[0,1],"E":[1,0],"S":[0,-1],"W":[-1,0]}
turns = {"L":-1,"R":1}
facing = "E"
start = [0,0]

for line in inputs:
    cmd = line[0]
    amt = int(line[1:])
    if cmd == "F":
        start = [start[0]+dirs[facing][0]*amt,start[1]+dirs[facing][1]*amt]
    elif cmd in dirs:
        start = [start[0]+dirs[cmd][0]*amt,start[1]+dirs[cmd][1]*amt]         
    elif cmd in turns:
        facing = list(dirs.keys())[(list(dirs.keys()).index(facing) + (turns[cmd]*amt//90))%4]
    
print("original instruction interpretation")
print(abs(start[0])+abs(start[1]))

waypoint = [10,1]
start = [0,0]

for line in inputs:
    cmd = line[0]
    amt = int(line[1:])
    if cmd == "F":
        start = [start[0]+waypoint[0]*amt,start[1]+waypoint[1]*amt]
    elif cmd in dirs:
        waypoint = [waypoint[0]+dirs[cmd][0]*amt,waypoint[1]+dirs[cmd][1]*amt]         
    elif cmd in turns:
        if amt == 180:
            waypoint = [-waypoint[0],-waypoint[1]]
        elif (amt == 90 and cmd == "L") or (amt == 270 and cmd == "R"):
            waypoint = [-waypoint[1],waypoint[0]]
        elif (amt == 90 and cmd == "R") or (amt == 270 and cmd == "L"):
            waypoint = [waypoint[1],-waypoint[0]]

print("back of card updated instructions")
print(abs(start[0])+abs(start[1]))
