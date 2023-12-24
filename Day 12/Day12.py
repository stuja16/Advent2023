# https://adventofcode.com/2023/day/12

import math, re
from functools import lru_cache

def solve(fileName,d1):
    total = 0

    for line in open(fileName,"r").read().strip().split('\n'):
        springs, notes = line.split(" ")
        if d1:
            total += getConfigs(springs, tuple(map(int,notes.split(","))))
        else:
            total += getConfigs(((springs + "?") * 5)[:-1], tuple(map(int,notes.split(","))) * 5)   # Repeat 5 times

    return total

@lru_cache(maxsize=None)    # Cache all function runs to speed up for part 2
def getConfigs(springs, notes):
    if not springs:
        return 1 if notes == () else 0
    elif notes == ():
        return 0 if "#" in springs else 1
    
    result = 0
    
    if springs[0] in ".?":
            result += getConfigs(springs[1:],notes)
    
    if springs[0] in "#?":
            if notes[0] <= len(springs) and "." not in springs[:notes[0]] and (notes[0] == len(springs) or springs[notes[0]] != "#"):
                result += getConfigs(springs[notes[0] + 1:], notes[1:])
    
    return result

#print(solve("Day 12\Day12_UnitTest.txt"))
#print(solve("Day 12\Day12_Input.txt", True))    # Part 1
print(solve("Day 12\Day12_Input.txt", False))   # Part 2