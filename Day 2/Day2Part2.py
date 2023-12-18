# https://adventofcode.com/2023/day/2

def totalIdValues(fileName):
    file = open(fileName,"r")
    sum = 0;    # Variable to store the sum (target value)
    for each in file:
        ps = cleanString(each)
        sum += ps
    print("Sum of the power of the sets of cubes:", sum)   # Print sum to the console
    file.close()

# Argument: One line from the input file, named 'text'
# Determines the game id as well as the maximum shown quantity of each colored cube
# Returns: Game ID number, max red cubes, max green cubes, max blue cubes
def cleanString(text):
    red = 0
    green = 0
    blue = 0

    text = text[text.find(":") + 2:text.find("\n")]     # Important to also trim off the \n from the string

    count = 0
    while len(text) > 0:
        count += 1
        next = text.find(" ")
        
        val = int(text[:next])
        text = text[next + 1:]

        comma = text.find(",")
        colon = text.find(";")
        if comma == colon:
            next = len(text)
        elif (comma < colon and comma >= 0) or colon == -1:
            next = comma
        else:
            next = colon
        color = text [:next]
        text = text [next + 2:]

        # Modify cube maximums if applicable
        if color == "red" and val > red:
            red = val
        elif color == "green" and val > green:
            green = val
        elif color == "blue" and val > blue:
            blue = val

        if count >= 20:     # Safety to avoid an infinite loop if code has errors
            raise ValueError('Loop appears to be infinite')
        
    return red * green * blue

totalIdValues("Day 2\Day2_Input.txt")