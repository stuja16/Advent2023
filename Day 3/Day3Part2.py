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
    numbers, gears = findKeyComponents(engine)
    gears = validateGears(numbers, gears, width)

    # Sum the valid gear ratios
    for gear in gears:
        if gear[0] == 2:
            sum += gear[1]
    #print(gears)
    print(sum)

def findKeyComponents(engine):
    numbers = []
    gears = []

    # Find and log part numbers
    pattern = re.compile(r'[0-9]+')
    matches = pattern.finditer(engine)
    for match in matches:
        # 1.Number value  2.Start index  3.End index
        numbers.append((int(match.group()), match.span()[0], match.span()[1]))

    # Find and log gears
    pattern = re.compile(r'[*]')
    matches = pattern.finditer(engine)
    for match in matches:
        # 1.Adj # count  2.Adj # product  3.Start index
        gears.append([0, 0, match.span()[0]])

    # Return the logs of both
    return numbers, gears

def validateGears(numbers, gears, width):
    for gear in gears:
        for num in numbers:
            val, start, end = num
            start -= width + 1
            end -= width - 1

            for j in range(3):
                # Move to next row down
                if j > 0:
                    start += width
                    end += width

                i = start
                while i < end:
                    if i == gear[2]:
                        gear[0] += 1    # First position tracks count of adjacent #s
                        #print("Adj #:",val,": Coord:",i)
                        if gear[1] == 0:    # Second position tracks product of adjacent # values
                            gear[1] += val
                        else:
                            gear[1] *= val
                    i += 1
    return gears
                
#totalPartNumbers("Day 3\Day3_UnitTest.txt")
totalPartNumbers("Day 3\Day3_Input.txt")