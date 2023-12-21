# https://adventofcode.com/2023/day/7

import re

def solve(fileName):
    steps, loc = (0, "AAA")

    # Read input from text file
    file = open(fileName,"r")
    text = file.read().strip().replace("(","").replace(")","").replace(" = ",", ").split("\n")
    file.close()

    del (text[1])   # Remove blank line
    guide = text.pop(0)
    text = [line.split(", ") for line in text]

    while not loc == "ZZZ":
        s, loc = travel(list(map("LR".index,guide)),text,loc) 
        steps += s
        print(steps)
    print("Total steps taken:",steps)
    

def travel(guide,lookup,loc):
    steps = 0
    for dir in guide:
        for start,left,right in lookup:
            if start == loc and dir == 0:
                loc = left
            elif start == loc and dir == 1:
                loc = right
            else:
                continue
            steps += 1
            break

        if loc == "ZZZ":
            break
    return steps,loc

#solve("Day 8\Day8_UnitTest1.txt")
#solve("Day 8\Day8_UnitTest2.txt")
solve("Day 8\Day8_Input.txt")