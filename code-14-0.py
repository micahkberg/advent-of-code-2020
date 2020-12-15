# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:03:47 2020

@author: micah

advent of code 12/14/2020
"""

import itertools


filename = "day14.txt"
f = open(filename, 'r')
inputs = f.read().split("\n")

memory = {}

for i in range(len(inputs)):
    inputs[i] = inputs[i].split(" = ")
    




def get_addr(string):
    return string[4:-1]

def mask_bin(dec_string,mask):
    num = str(bin(int(dec_string)))[2:]
    new_num = ""
    for i in range(1,len(mask)+1):
        #print(str(i)+" , "+new_num)
        if mask[-i] == "X" and i>len(num):
            new_num = "0" + new_num
        elif mask[-i] != "X":
            new_num = mask[-i]+new_num
        else:
            new_num = num[-i] +new_num
    #print("converted "+dec_string+" to "+new_num)   
    exit_num = 0
    for i in range(0,len(new_num)):
        exit_num += int(new_num[-(i+1)]) * (2**i)
    #print(exit_num)
    #print(bin(exit_num))
    return(exit_num)
    
    

#part 1
#for line in inputs:
#    #print(line)
#    if line[0] == "mask":
#        mask = line[1]
#        #print(mask)
#    else:
#        memory[get_addr(line[0])] = mask_bin(line[1],mask)
        

#print(sum(memory.values()))

#part 2
def flicker(bin_num):
    output_nums = []
    xs = bin_num.count("X")
    
    variations = itertools.product(["1","0"],repeat=xs)
    
    for variation in variations:
        new_num = ""
        count = 0
        for i in bin_num:
            if i != "X":
                new_num += i
            else:
                new_num += variation[count]
                count+=1
        output_nums.append(new_num)
    return output_nums


def memory_mask(dec,mask):

    num = str(bin(dec))[2:].rjust(36,"0")
    #print("address in binary: " + num)
    #print("masking...")
    new_num = ""
    for i in range(len(mask)):
        #print("in   "+num[:i+1])
        #print("mask "+mask[:i+1])
        
        
        if mask[i] == "0":
            new_num += num[i]

        elif mask[i] == "1":
            new_num +="1"
        else:
            new_num +="X"
        
    if len(new_num)>36:
        print("initial address length too long...")
            
        #print("out  "+new_num)
    
    addr_list = flicker(new_num)
    
    return(addr_list)
    
    #exit_num = 0
    #for i in range(0,len(new_num)):
    #    exit_num += int(new_num[-(i+1)]) * (2**i)
    #print(exit_num)
    #print(bin(exit_num))
    #return(exit_num)

debug_data = []
for line in inputs:
    
    if line[0] == "mask":
        mask = line[1]
        
        #print("new mask...")
    elif line != [""]:
        
    
            

        address_dec = int(get_addr(line[0]))
        #print("getting addresses at " +str(address_dec)+" ...")
        addrs = memory_mask(address_dec,mask)
        #print("addresses acquired, count:")
        #print(len(addrs))
        for addr in addrs:
            memory[addr] = int(line[1])
            
        debug_data.append([2**mask.count("X"),len(addrs)])
        
print(sum(memory.values()))