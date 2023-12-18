MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

def totalIdValues(fileName):
    file = open(fileName,"r")
    sum = 0;    # Variable to store the sum (target value)
    for each in file:
        id = cleanString(each)
        sum += id
    print("Sum of all ID values of possible games:", sum)   # Print sum to the console
    file.close()

# Argument: One line from the input file, named 'text'
# Determines if the shown values were possible based on the real quantities
# Returns: Games ID if the game is possible, 0 if the game is impossible
def gamePossible(text): 
    id, r, g, b = cleanString(text)
    if r > MAXRED or g > MAXGREEN or b > MAXBLUE:
        return 0
    else:
        return id

# Argument: One line from the input file, named 'text'
# Determines the game id as well as the maximum shown quantity of each colored cube
# Returns: Game ID number, max red cubes, max green cubes, max blue cubes
def cleanString(text):
    possible = True

    text = text[5:] # Remove 'Game ' from string
    id = int(text[:text.find(":")]) # Get game ID#
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
        if color == "red" and val > MAXRED:
            possible = False
        elif color == "green" and val > MAXGREEN:
            possible = False
        elif color == "blue" and val > MAXBLUE:
            possible = False

        if count >= 20:     # Safety to avoid an infinite loop if code has errors
            raise ValueError('Loop appears to be infinite')
        
    if possible:
        return id
    else:
        return 0

totalIdValues("Day 2\Day2_Input.txt")