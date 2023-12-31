# https://adventofcode.com/2023/day/8

# Solution improved with help from the solutions subreddit:
#       https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kcguu6a/

import re

def solve(fileName):
    global guide, text
    steps, loc = (0, "AAA")

    # Read input from text file
    file = open(fileName,"r")
    text = file.read().strip().replace("(","").replace(")","").replace(" = ",", ").split("\n")
    file.close()

    del (text[1])   # Remove blank line
    guide = text.pop(0)
    text = [line.split(", ") for line in text]

    print(travel(loc))
    
def travel(loc, i=0):
    while not loc.endswith("Z"):
        dir = guide[i % len(guide)]
        for set in text:
            s,*next = set
            if loc == s:
                loc = next[dir=="R"]
        i += 1
    return i

#solve("Day 8\Day8_UnitTest1.txt")
#solve("Day 8\Day8_UnitTest2.txt")
solve("Day 8\Day8_Input.txt")