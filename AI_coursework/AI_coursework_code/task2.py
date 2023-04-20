import random


# positions in the world that are walkable (i.e. not out of bounds), shown by tuple[row, column]
valid_positions = [
            (1, 1), (1, 2), (2, 1), (2, 2),
            (2, 3), (2, 4), (3, 2), (3, 3),
            (3, 4), (4, 3), (4, 4)
        ]


def display(world):

    print()
    for i in world:
        print(*i)
    print()


class Goal:
    def __init__(self, world):
        self.row = 4
        self.column = 4
        world[self.row][self.column] = "G"


class Box:
    def __init__(self, world):
        self.row = 2
        self.column = 2
        world[self.row][self.column] = "B"

    def covers_goal(self, goal: Goal) -> bool:
        """
        The box can never cover the goal but this is how it could be implemented in a more open world.

        :param goal: goal object
        :return: true if box covers goal
        """

        if (self.row, self.column) == (goal.row, goal.column):
            return True
        return False

    def goes_out_of_bounds(self, direction: str) -> bool:
        """
        Checks to see if the box gets pushed out of bounds, prints "out of bounds" to signal this.
        Method is called by the agent when it moves.

        :param direction: str of direction ("north", "south", "east", ""west")
        :return: true if the box will be pushed over the threshold
        """

        # init variables for conditions
        future_row: int
        future_column: int

        # if the row to the north (self.row - 1) will bring the box out of bounds, return true
        if direction == "north":
            future_row = self.row - 1
            return True if (future_row, self.column) not in valid_positions else False

        # same premise as above but for all other directions
        elif direction == "south":
            future_row = self.row + 1
            return True if (future_row, self.column) not in valid_positions else False

        elif direction == "east":
            future_column = self.column + 1
            return True if (self.row, future_column) not in valid_positions else False

        elif direction == "west":
            future_column = self.column - 1
            return True if (self.row, future_column) not in valid_positions else False

    def move_north(self, world) -> None:

        self.row -= 1
        world[self.row][self.column] = "B"

    def move_south(self, world) -> None:

        self.row += 1
        world[self.row][self.column] = "B"

    def move_east(self, world) -> None:

        self.column += 1
        world[self.row][self.column] = "B"

    def move_west(self, world) -> None:

        self.column -= 1
        world[self.row][self.column] = "B"


class Agent:

    def __init__(self, world):

        self.row = 1
        self.column = 2
        world[self.row][self.column] = "A"
        self.goal_reached = False
        self.step_count = 0
        self.push_count = 0  # amount of times we push the box

    def check_for_box(self, direction: str, box: Box) -> bool:
        """
        Sensor for box object, can see in all four directions

        :param direction: str direction ("north", "south", "east", "west")
        :param box: box object that we try to sense
        :return: true if the box is one cell to the north/south/east/west, whichever way we check
        """

        future_box_row: int
        future_box_column: int

        # check to see if one cell above is the box object, returns true if this is the case
        if direction == "north":
            future_row = self.row - 1
            return True if (future_row, self.column) == (box.row, box.column) else False

        # same premise as above from here
        elif direction == "south":
            future_row = self.row + 1
            return True if (future_row, self.column) == (box.row, box.column) else False

        elif direction == "east":
            future_column = self.column + 1
            return True if (self.row, future_column) == (box.row, box.column) else False

        elif direction == "west":
            future_column = self.column - 1
            return True if (self.row, future_column) == (box.row, box.column) else False

    def check_for_goal(self, goal: Goal) -> bool:
        """
        The goal can only be approached by agent moving south or east

        :param world: final grid world
        :return: str "south" or "east"
        """

        if (self.row, self.column) == (goal.row, goal.column):
            return True

        return False

    def goes_out_of_bounds(self, direction: str) -> bool:
        """
        Checks to see if the agent will go out of bounds if it moves in the direction specified, called in the
        methods that control agent movement.

        :param direction: str ("north", "south", "east", "west")
        :return: true if the agent will go out of bounds in the specified direction
        """

        future_row: int
        future_column: int

        # if the row to the north (self.row - 1) will bring the box out of bounds, return true
        if direction == "north":
            future_row = self.row - 1
            return True if (future_row, self.column) not in valid_positions else False

        # same for all other directions
        elif direction == "south":
            future_row = self.row + 1
            return True if (future_row, self.column) not in valid_positions else False

        elif direction == "east":
            future_column = self.column + 1
            return True if (self.row, future_column) not in valid_positions else False

        elif direction == "west":
            future_column = self.column - 1
            return True if (self.row, future_column) not in valid_positions else False


    def step_north(self, world: list, box: Box) -> None:
        """
        Agent move on cell to the north, will be able to push the box with it. Method accommodates if the agent or box
        will go out of bounds

        :param world: final grid world
        :param box: box object
        :return: None
        """

        # bounce back if agent will go out of bounds
        if self.goes_out_of_bounds("north"):
            print("Out of bounds, bounce back")
            return

        # if we can push the box, make sure it doesn't go out of bounds
        if self.check_for_box("north", box) and not box.goes_out_of_bounds("north"):
            print("pushing box north")
            box.move_south(world)
            self.push_count += 1

        # if the box will go out of bounds in the direction the agent pushes it, neither box nor agent can move
        elif self.check_for_box("north", box) and box.goes_out_of_bounds("north"):
            print("box out of bounds")
            return

        # normal movement for the agent
        self.row -= 1
        world[self.row][self.column] = "A"
        world[self.row + 1][self.column] = "."
        self.step_count += 1

    def step_south(self, world: list, box: Box) -> None:
        """
        Agent move on cell to the south, will be able to push the box with it. Method accommodates if the agent or box
        will go out of bounds

        :param world: final grid world
        :param box: box object
        :return: None
        """

        # bounce back if agent will go out of bounds
        if self.goes_out_of_bounds("south"):
            print("Out of bounds, bounce back")
            return

        # if we can push the box, make sure it doesn't go out of bounds
        if self.check_for_box("south", box) and not box.goes_out_of_bounds("south"):
            print("pushing box south")
            box.move_south(world)
            self.push_count += 1

        # if the box will go out of bounds in the direction the agent pushes it, neither box nor agent can move
        elif self.check_for_box("south", box) and box.goes_out_of_bounds("south"):
            print("box out of bounds")
            return

        # normal movement for the agent
        self.row += 1
        world[self.row][self.column] = "A"
        world[self.row - 1][self.column] = "."
        self.step_count += 1

    def step_east(self, world: list, box: Box) -> None:
        """"
        Agent move on cell to the east, will be able to push the box with it. Method accommodates if the agent or box
        will go out of bounds

        :param world: final grid world
        :param box: box object
        :return: None
        """

        # bounce back if agent will go out of bounds
        if self.goes_out_of_bounds("east"):
            print("Out of bounds, bounce back")
            return

        # if we can push the box, make sure it doesn't go out of bounds
        if self.check_for_box("east", box) and not box.goes_out_of_bounds("east"):
            print("pushing box east")
            box.move_east(world)
            self.push_count += 1

        # if the box will go out of bounds in the direction the agent pushes it, neither box nor agent can move
        elif self.check_for_box("east", box) and box.goes_out_of_bounds("east"):
            print("box out of bounds")
            return

        # normal movement for the agent
        self.column += 1
        world[self.row][self.column] = "A"
        world[self.row][self.column - 1] = "."
        self.step_count += 1

    def step_west(self, world: list, box: Box) -> None:
        """
        Agent move on cell to the west, will be able to push the box with it. Method accommodates if the agent or box
        will go out of bounds

        :param world: final grid world
        :param box: box object
        :return: None
        """

        # bounce back if agent will go out of bounds
        if self.goes_out_of_bounds("west"):
            print("Out of bounds, bounce back")
            return

        # if we can push the box, make sure it doesn't go out of bounds
        if self.check_for_box("west", box) and not box.goes_out_of_bounds("west"):
            print("pushing box west")
            box.move_west(world)
            self.push_count += 1

        # if the box will go out of bounds in the direction the agent pushes it, neither box nor agent can move
        elif self.check_for_box("west", box) and box.goes_out_of_bounds("west"):
            print("box out of bounds")
            return

        # normal movement for the agent
        self.column -= 1
        world[self.row][self.column] = "A"
        world[self.row][self.column + 1] = "."
        self.step_count += 1

    def walk(self, world: list, box: Box, goal: Goal) -> None:
        """
        Where the magic happens, agent chooses a random direction (north/south/east/west) and moves in that
        direction, pushing the box with it. Agent will stop walking if it reaches the goal. Method calls
        itself recursively so the agent can keep moving.

        :param world: final grid world
        :param box: box object
        :param goal: goal object
        :return:
        """

        display(world)

        if self.goal_reached:
            print(f"goal reached in {self.step_count} steps")
            return

        # this can never really happen but it could be implemented this way
        if box.covers_goal(goal):
            print("box covers goal, game over")
            return

        directions = ["north", "south", "east", "west"]
        choice = random.choice(directions)

        if choice == "north":
            print("moving north")
            self.step_north(world, box)
            self.walk(world, box, goal)

        elif choice == "south":
            print("moving south")
            if self.check_for_goal(goal):
                self.goal_reached = True
            self.step_south(world, box)
            self.walk(world, box, goal)

        elif choice == "east":
            print("moving east")
            if self.check_for_goal(goal):
                self.goal_reached = True
            self.step_east(world, box)
            self.walk(world, box, goal)

        else:
            print("moving west")
            self.step_west(world, box)
            self.walk(world, box, goal)


def main():

    """
    valid_positions = [
            (1, 1), (1, 2), (2, 1), (2, 2),
            (2, 3), (2, 4), (3, 2), (3, 3),
            (3, 4), (4, 3), (4, 4)
        ]
    """

    world = [['x' if (row, col) not in valid_positions else '.' for col in range(6)] for row in range(6)]
    agent = Agent(world)
    box = Box(world)
    goal = Goal(world)
    agent.walk(world, box, goal)


if __name__ == "__main__":
    main()
