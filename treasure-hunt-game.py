import random

GRID_SIZE = 8


# Class to define location with X and Y coordinates
# list of function:
# 1. coordinate_to_string -> convert coordinate that contains int to string
# 2. is_equal_to -> function to check if player coordinates is equal with treasure or obstacle
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinate_to_string(self):
        return "({}, {})".format(self.x, self.y)

    def is_equal_to(self, pt):
        if not pt:
            return False

        if (self.x == pt.x) and (self.y == pt.y):
            return True

        return False


# function to get location with list of position and position
# it will return te position or -1 if not found
def find_point(used_location, pt):
    for i in range(0, len(used_location)):
        if used_location[i].is_equal_to(pt):
            return i

    return -1


# function to choose random location especially for the treasures
def choose_occupied_location(used_location):
    while True:
        location = Point(random.randint(1, GRID_SIZE), random.randint(1, GRID_SIZE))

        if find_point(used_location, location) < 0:
            used_location.append(location)

            return location


treasures = ['diamond', 'gold', 'silver', 'bronze']
treasure_location = []
obstacle_location = [Point(3, 5), Point(3, 3), Point(4, 3), Point(5, 3), Point(5, 4), Point(7, 4)]
player_location = Point(0, 0)
treasures_founded = 0


# function to handle player entering location
def enter_location(location):
    global player_location
    global treasure_location
    global treasures_founded
    global obstacle_location

    player_location = location

    print("You are here now {}".format(player_location.coordinate_to_string()))

    # determine treasures locations
    treasure = find_point(treasure_location, player_location)

    # determine obstacles locations
    obstacle = find_point(obstacle_location, player_location)

    # check the obstacles
    if obstacle >= 0:
        print("There's an obstacle!")
        return False

    # check founded treasures
    if treasure >= 0:
        print("You find {}".format(treasures[treasure]))

        treasures[treasure] = None

        treasures_founded += 1

        if treasures_founded == len(treasures):
            print("You found all treasures!")

            return False

        else:
            remain_treasures = len(treasures) - treasures_founded

            print("You get {} treasures, remain {}".format(treasures_founded, remain_treasures))

    return True


# function to define player commands
def command_tools(command):
    command = command.lower()

    if not command:
        print("Please, input the directions!")

    if command == "exit":
        return False

    new_location = None

    # check possible player movement
    if command == "a":
        if player_location.y > 1:
            new_location = Point(player_location.x, player_location.y - 1)
    elif command == "b":
        if player_location.x < GRID_SIZE:
            new_location = Point(player_location.x + 1, player_location.y)
    elif command == "c":
        if player_location.y < GRID_SIZE:
            new_location = Point(player_location.x, player_location.y + 1)
    elif command == "help":
        print("""Details:
        1. # represents an obstacle.
        2. . represents a clear path.
        3. X represents the player’s starting position.

        Commands:
        1.  Up/North A step(s), then
        2.  Right/East B step(s), then
        3. Down/South C step(s).""")
    else:
        print("Wrong command!")

        return True

    if not new_location:
        print("You can't move there!")

        return True

    return enter_location(new_location)


def game_start_loop():
    the_grid = """
        ########
        #......#
        #.###..#
        #...#.##
        #X#....#
        ########
    """
    print(the_grid)
    active_game = enter_location(player_location)
    while active_game:
        print("\nWhat do you want to do? (need help? please, enter 'help')")

        option = input()

        active_game = command_tools(option)


def init_game():
    global player_location
    global treasure_location
    global treasures_founded

    treasures_founded = 0

    # set the player in bottom left position
    player_location = Point(2, 5)
    occupied_locations = [player_location]

    # generate randon location for treasures
    for i in range(0, len(treasures)):
        treasure_location.append(choose_occupied_location(occupied_locations))


init_game()
game_start_loop()

print("Thanks for playing!")
