# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:22:27 2020

@author: micah

advent of code 12/18/2020

part 1

this evaluates addition and multiplication as though they were at the same precedence level
"""


filename = "day18.txt"
f = open(filename, 'r')
homework = f.read().split("\n")



def map_parens(problem):
    guide = []
    for ind in range(len(problem)):
        char = problem[ind]
        if char == "(" or char ==")":
            guide.append([char,ind])
    return(guide)
            
        
    

def reduce(problem):
    if "(" not in problem:
        return problem
    else:
        # guide -> [paren char , index in problem]
        paren_guide = map_parens(problem)
        for i in range(len(paren_guide)-1):
            if paren_guide[i][0] == "(" and paren_guide[i+1][0]==")":
                front = problem[0:paren_guide[i][1]]
                #middle = problem[paren_guide[i][1]+1:paren_guide[i+1][1]]
                middle = solve(problem[paren_guide[i][1]+1:paren_guide[i+1][1]])
                back = problem[paren_guide[i+1][1]+1:]
                output = front + middle + back
                return reduce(output)
                
                
        

def solve(problem):
    simp_problem = reduce(problem) + " "
    total = 0
    next_num = ""
    next_op = None
    for i in simp_problem:
        if i == " " and next_num != "":
            if total == 0:
                total = int(next_num)
            elif next_op == "*":
                total *= int(next_num)
            elif next_op == "+":
                total += int(next_num)
            next_num = ""
        elif i==" ":
            pass
        elif i == "*" or i == "+":
            next_op = i
        else:
            next_num += i
            
                    
            
    return(str(total))

def main():
    solutions = []
    for problem in homework:
        solutions.append(solve(problem))
    print(solutions)    
    out = 0
    for i in solutions:
        out += int(i)
    print(out)
main()
        
#wrong answers...
#328163 (low) some equations were not evaluating all operations for a reason that i have forgotten
#1280309 (still low) was processing multiple digit numbers wrong
#2062853320 (still low) wasnt performing last operation in an equation, added a space to each line lol
#202553439706 (correct!)