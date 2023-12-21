# https://adventofcode.com/2023/day/8

# Solution improved with help from the solutions subreddit:
#       https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kcguu6a/

import math, re

def solve(fileName):
    global guide, text
    starts, locs = ("",[])

    # Read input from text file
    file = open(fileName,"r")
    text = file.read().strip().replace("(","").replace(")","").replace(" = ",", ").split("\n")
    file.close()

    del (text[1])   # Remove blank line
    guide = text.pop(0)
    text = [line.split(", ") for line in text]
    pattern = re.compile(r'\w\wA')
    for dir in text:
        starts += dir[0] + " "
    matches = pattern.finditer(starts)
    for match in matches:
        locs.append(match.group())
    
    print(math.lcm(*map(travel, locs)))

def travel(loc, i=0):
    while not loc.endswith("Z"):
        dir = guide[i % len(guide)]
        for set in text:
            s,*next = set
            if loc == s:
                loc = next[dir=="R"]    # Using a boolean to index a 2-element array
                break
        i += 1
    return i

#solve("Day 8\Day8_UnitTest3.txt")
solve("Day 8\Day8_Input.txt")