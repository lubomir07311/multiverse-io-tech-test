import re

GRID_REGEX = r"^[0-9]+\s[0-9]+$"
INPUT_REGEX = r"^\([0-9]+,\s[0-9]+,\s[NESW]+\)\s+[LFR]+$"
ROBOTS_TO_RUN = 2
MOVES = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def move(x, y, direction, grid_x, grid_y):
    move_x, move_y = MOVES[direction]
    x += move_x
    y += move_y
    if x < 0 or x > grid_x or y < 0 or y > grid_y:
        return x - move_x, y - move_y, True
    return x, y, False


def get_grid_size():
    while True:
        user_input = input("Enter grid size: ")
        if re.match(GRID_REGEX, user_input):
            grid_x, grid_y = map(int, user_input.split())
            return grid_x, grid_y
        else:
            print(
                "Invalid input. Please enter a grid size 'x y' where x and y are integers: "
            )


def get_robot_config():
    while True:
        user_input = input("Enter position, orientation and commands: ")
        if re.match(INPUT_REGEX, user_input):
            input_list = (
                user_input.replace("(", "").replace(")", "").replace(",", "").split()
            )
            posX, posY, direction, commands = (
                int(input_list[0]),
                int(input_list[1]),
                input_list[2],
                input_list[3],
            )
            directions = ["N", "E", "S", "W"]
            while directions[0] != direction:
                directions = directions[1:] + directions[:1]
            return posX, posY, commands, directions
        else:
            print(
                "Invalid input. Please enter a string in the following format: (n, n, D) C where n is a number, D is one of N E S W, C is one of L F R, repeated as many times as desired: "
            )


def main():
    outputs = []
    grid_x, grid_y = get_grid_size()

    for i in range(ROBOTS_TO_RUN):
        posX, posY, commands, directions = get_robot_config()
        for command in commands:
            if command == "F":
                posX, posY, is_lost = move(posX, posY, directions[0], grid_x, grid_y)
                if is_lost:
                    break
            elif command == "R":
                directions = directions[1:] + directions[:1]
            elif command == "L":
                directions = directions[-1:] + directions[:-1]

        output = f"({posX}, {posY}, {directions[0]})"
        if is_lost:
            output += " LOST"
        outputs.append(output)

    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
