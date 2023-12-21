# https://adventofcode.com/2023/day/9

import math, re

def solve(fileName):
    sum = 0

    file = open(fileName,"r").read().strip().split('\n')
    list = [n for n in [re.findall(r'-?\d+', s) for s in file]]
    for s in list:
        sum += predictSequence([int(n) for n in s][::-1])   # Reverse sequence
    return sum

def predictSequence(seq):
    nextSeq = [b-a for a,b in zip(seq, seq[1:])]     # "zip" function creates a tuple
    return 0 if all(s == 0 for s in seq) else seq[-1] + predictSequence(nextSeq)

#print(solve("Day 9\Day9_UnitTest.txt"))
print(solve("Day 9\Day9_Input.txt"))