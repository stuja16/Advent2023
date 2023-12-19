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

    # Separate indiv. seeds and map each to a location
    pattern = re.compile('[0-9]+')
    matches = pattern.finditer(seeds)
    for match in matches:
        val = int(match.group())
        # Do as many mappings as possible/needed
        for map in mappings:
            val = mapValues(val, map)
        locations.append(val)
    
    print(min(locations))

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

# Input (val): Integer representing the source/starting value
# Input (map): list of all available mapping values for the current transformation
# Output: an integer successfully mapped from the source value (destination value)
def mapValues(val, map):
    for line in map:
        # Clean up the values
        destination, source, range = line
        destination = int(destination)
        source = int(source)
        range = int(range)

        # If a mapping matches the input "val", return corresponding destination value
        if source <= val and val <= source + range:
            return destination + val - source
    # Else, return input "val"
    return val

#getLowestLocation("Day 5\Day5_UnitTest.txt")
getLowestLocation("Day 5\Day5_Input.txt")