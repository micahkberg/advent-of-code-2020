# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:22:27 2020

@author: micah

advent of code 12/18/2020

part 2, evaluates addition at a higher precedence level than multiplication
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
            
        
    

def reduce_parens(problem):
    if "(" not in problem:
        return problem
    elif "(" in problem:
        # guide -> [paren char , index in problem]
        paren_guide = map_parens(problem)
        for i in range(len(paren_guide)-1):
            if paren_guide[i][0] == "(" and paren_guide[i+1][0]==")":
                front = problem[0:paren_guide[i][1]]
                #middle = problem[paren_guide[i][1]+1:paren_guide[i+1][1]]
                middle = solve(problem[paren_guide[i][1]+1:paren_guide[i+1][1]])
                back = problem[paren_guide[i+1][1]+1:]
                output = front + middle + back
                return reduce_parens(output)
            

    
                
def addends_first(problem):
    multipliers = []
    last_num = ""
    current_sum = 0
    next_op = None
    pos = 0
    for i in problem:
        
        if i == " " and last_num != "":
            current_sum += int(last_num)
            last_num = ""
            if pos == len(problem)-1:
                multipliers.append(current_sum)
                
        elif i ==  " " and last_num == "" and current_sum > 0 and next_op == '*':
            multipliers.append(current_sum)
            current_sum = 0

        elif i ==" ":
            pass
        elif i == "*" or i=="+":
            next_op = i
        else:
            last_num += i
            
            

        pos+=1
    prod = 1
    for i in multipliers:
        prod *= i
    return prod

        

def solve(problem):
    simp_problem = reduce_parens(problem) + " "
    return(str(addends_first(simp_problem)))


def main():
    solutions = []
    for problem in homework:
        solutions.append(solve(problem))
    print(solutions)    
    out = 0
    for i in solutions:
        out += int(i)
    print(out)
    print(len(solutions))
    print(len(homework))
main()
        
#wrong answers...
#3556978138 (low) fixed a problem where it wasnt adding both ends a multiplying problem into the product list
#964894998361547 (high) switching back from multiplying to adding was broken?
#352862335976 (low) trying to fix last number problems
#5213579544490 still bad
#575055884832
#21967439 damn
#88534268715687