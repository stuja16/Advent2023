# https://adventofcode.com/2023/day/1

import re

# Sums calibration values for each line
def solve(p1 = True):   # If running part 2, set p1 = False
    lines = [textToDigit(l) if not p1 else l for l in open("Day 1\Day1_Input.txt","r").read().strip().split("\n")]
    print("Sum of all Callibration Values:", sum([int(n[0] + n[-1]) for n in ["".join(re.findall("\d+", l)) for l in lines]]))

# Replaces all written numbers with numeric digits, preserving first and last character for overlapping numbers
def textToDigit(text):
    digitTexts = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
    for word,num in digitTexts.items():
        text = text.replace(word,num)
    return text

solve()         # part 1
solve(False)    # part 2