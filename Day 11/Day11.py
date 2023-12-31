# https://adventofcode.com/2023/day/11

import math, re

def solve(fileName,scale):
    grid = open(fileName,"r").read().strip().split('\n')
    empty_rows = [r for r,row in enumerate(grid) if all(ch == "." for ch in row)]
    empty_cols = [c for c,col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]
    galaxies = [(r,c) for r,row in enumerate(grid) for c,ch in enumerate(row) if ch == "#"]

    total = 0
    for i, (r1,c1) in enumerate(galaxies):
        for (r2,c2) in galaxies[i+1:]:
            for r in range(min(r1,r2),max(r1,r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1,c2),max(c1,c2)):
                total += scale if c in empty_cols else 1
    return total

#print(solve("Day 11\Day11_UnitTest.txt",10))
#print(solve("Day 11\Day11_Input.txt",2))           # Part 1
print(solve("Day 11\Day11_Input.txt",1000000))     # Part 2