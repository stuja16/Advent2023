# https://adventofcode.com/2023/day/5

import re

def getLowestLocation(fileName):
    text = ""
    mappings = []
    locations = []

    # Read input from text file
    file = open(fileName,"r")
    for line in file:
        text += line
    file.close()

    # Clean up input text before searching
    text = text[7:]
    text = text.split(":")
    seeds = text[0]
    text = text[1:]

    # Clean mappings to make them useable
    for map in text:
        mappings.append(cleanMappingValues(map))

    # Get the range pairs of input seed and add them to a list
    pattern = re.compile('[0-9]+ [0-9]+')
    matches = pattern.finditer(seeds)
    for match in matches:
        start, range = match.group().split(" ")
        start = int(start)
        end = int(range) + start
        locations.append((start, end))

    # Map the entire input list as many times as there are mappings
    for map in mappings:
        locations = mapValues(locations, map)
    
    # Find minimum location
    print("Minimum Location:",min(locations)[0])

# Input (map): string representing a list of one type of mapping values (AKA seed-to-soil)
# Output: list of mapping values (destination, source, range)
def cleanMappingValues(map):
    mappingValues = []
    pattern1 = re.compile('[0-9]+ [0-9]+ [0-9]+')
    pattern2 = re.compile('[0-9]+')

    matches1 = pattern1.finditer(map)
    for match in matches1:
        valueSet = []
        matches2 = pattern2.finditer(match.group())
        for each in matches2:
            valueSet.append(each.group())
        mappingValues.append(valueSet)
    
    return mappingValues

# Input (vals): List of tuples of integers the source starting value and ending values
# Input (map): list of all available mapping values for the current transformation
# Output: a list of tuples of integers successfully mapped from the source value to the destination value
def mapValues(vals, map):
    oldVals = vals
    newVals = []
    mapSets = len(map)
    i = 0
    while len(oldVals) > 0:
        i += 1
        start, end = oldVals.pop(0)
        for line in range(mapSets):
            # Clean up the values
            destination, source, length = map[line]
            d1 = int(destination)
            s1 = int(source)
            length = int(length)
            d2 = d1 + length
            s2 = s1 + length

            # If a mapping matches the input "val", return corresponding destination value
            if s1 <= start and end <= s2:   # x is contained in y, or x == y
                newVals.append((d1+start-s1,d2-(s2-end)))
            elif s1 <= start and start < s2 and s2 < end:   # x starts in y
                newVals.append((d1+start-s1, d2))
                oldVals.append((s2, end))
            elif start <= s1 and s1 < end and end <= s2:    # x ends in y
                newVals.append((d1, d1+end-s1))
                oldVals.append((start,s1))
            elif start <= s1 and s2 <= end:     # y is contained in x, or x == y
                newVals.append((d1,d2))
                oldVals.append((start,s1))
                oldVals.append((s2,end))
            elif line == len((map)) - 1:    # If it is the last mapSet, set output range to input range
                newVals.append((start,end))
            else:
                continue
            break
    return cleanRanges(newVals)

# Input (vals): List of tuples of integers representing ranges of values
# Output: A similar list, but shortened wherever two ranges met each other if possible
def cleanRanges(vals):
    output = vals

    changed = True
    while changed:
        changed = False
        vals = output
        output = []

        # Search criteria from i-index, search within j-index
        for i in range(len(vals)):
            # If a change has already happened, just append the remaining pais
            if changed and i < len(vals):
                output.append(vals[i])
                continue

            # If no change has happened, continue looking for a match
            for j in range(i+1, len(vals)):
                if vals[i][1] == vals[j][0]:
                    output.append((vals[i][0],vals[j][1]))
                    del(vals[j])
                elif vals[i][0] == vals[j][1]:
                    output.append((vals[j][0],vals[i][1]))
                    del(vals[j])
                elif j == len(vals)-1:
                    output.append(vals[i])
                    continue
                else:   # If no change was found, continue to next pair to search
                    continue
                changed = True
                break
    return vals     # Once no more changes are possible, return full list

#getLowestLocation("Day 5\Day5_UnitTest.txt")
getLowestLocation("Day 5\Day5_Input.txt")