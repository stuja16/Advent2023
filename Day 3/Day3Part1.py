# https://adventofcode.com/2023/day/3

import re

def totalPartNumbers(fileName):
    file = open(fileName,"r")
    sum = 0;    # Variable to store the sum (target value)
    engine = ""
    width = 0
    for each in file:   # Set our engine to include all the provided information w/o "\n"s and with buffer "."s
        i = each.find("\n")

        if engine == "":
            for j in range(i+3):
                engine += "."

        if i >= 0:
            width = i + 2
            engine += each[:i] + ".."
        else:
            engine += each + "."
    
    file.close()
    print("Sum of all part numbers:", cleanString(engine, width))

def cleanString(engine, width):
    sum = 0
    pattern = re.compile(r'[0-9]+')

    matches = pattern.finditer(engine)  # Search for the numbers in the string

    for match in matches:
        i = match.span()
        sum += validateNumber(engine, (False, int(match.group()), i[0], i[1]), width)
    return sum

def validateNumber(engine, number, width):
    valid, value, i1, i2 = number
    a = i1 - width - 1
    b = i2 - width + 1
    
    pattern = re.compile(r'[^0-9.]')    # Look for anything except #s and .s, AKA symbols

    for j in range(3):
        match = pattern.search(engine[a:b])

        if match != None:   # If symbol is found, set related # to a part #
            valid = True

        a += width
        b+= width

    if valid:
        return value
    else:
        return 0

#totalPartNumbers("Day 3\Part1_UnitTest.txt")
totalPartNumbers("Day 3\Day3_Input.txt")