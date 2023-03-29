import re
GRID_REGEX = r"[0-9]+\s[0-9]+"
INPUT_REGEX = r"\([0-9]+,\s[0-9]+,\s[NESW]+\)\s+[LFR]+"
DIRECTION_LIST = ['N', 'E', 'S' , 'W']
LOST = False

while True:
    user_input = input("Enter grid size: ")
    if re.match(GRID_REGEX, user_input):
        gridX, gridY = map(int, user_input.split())
        break
    else:
        print("Invalid input. Please enter a grid size 'x y' where x and y are integers: ")

while True:
    user_input = input("Enter a string: ")
    if re.match(INPUT_REGEX, user_input):
        input_list = user_input.replace('(','').replace(')','').replace(',','').split();
        startWidth, startHeight, direction, commands = int(input_list[0]), int(input_list[1]), input_list[2], input_list[3]
        while DIRECTION_LIST[0] != direction:
            DIRECTION_LIST = DIRECTION_LIST[1:] + DIRECTION_LIST[:1]
        break
    else:
        print("Invalid input. Please enter a string in the following format: (n, n, D) C where n is a number, D is one of N E S W, C is one of L F R, repeated as many times as desired: ")

for command in commands:
    if command == "F":
        if DIRECTION_LIST[0] == "N":
            if startHeight == gridY:
                LOST = True
                break
                
            startHeight += 1 
        elif DIRECTION_LIST[0] == "E":
            if startWidth == gridX:
                LOST = True
                break

            startWidth += 1
        elif DIRECTION_LIST[0] == "S":
            if startHeight == 0:
                LOST = True
                break
                
            startHeight -= 1
        elif DIRECTION_LIST[0] == "W":
            if startWidth == 0:
                LOST = True
                break

            startWidth -= 1
        
    elif command == "R":
        DIRECTION_LIST = DIRECTION_LIST[1:] + DIRECTION_LIST[:1]

    elif command == "L":
        DIRECTION_LIST = DIRECTION_LIST[-1:] + DIRECTION_LIST[:-1]
print (startWidth, startHeight, DIRECTION_LIST[0], LOST)
        
#(1, 2, W) LLRRLRF