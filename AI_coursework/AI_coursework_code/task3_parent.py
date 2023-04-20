
# tuples of row, column that are on the walkable path
valid_positions = [
            (1, 1), (1, 2), (1, 3), (2, 1),
            (2, 3), (3, 1), (3, 2), (3, 3)
        ]

class ArrowTiles:

    def __init__(self, world):

        self.right_arrow = (1, 2)
        self.left_arrow = (3, 2)
        self.down_arrow = (2, 3)
        self.up_arrow = (2, 1)

        world[self.right_arrow[0]] [self.right_arrow[1]] = "→"
        world[self.left_arrow[0]] [self.left_arrow[1]] = "←"
        world[self.down_arrow[0]] [self.down_arrow[1]] = "↓"
        world[self.up_arrow[0]] [self.up_arrow[1]] = "↑"

    def redraw_right_arrow(self, world) -> None:
        """
        If agent writes over the arrow when it moves through the world, this will redraw that arrow.
        """

        world[self.right_arrow[0]][self.right_arrow[1]] = "→"

    def redraw_left_arrow(self, world):
        """
        If agent writes over the arrow when it moves through the world, this will redraw that arrow.
        """

        world[self.left_arrow[0]][self.left_arrow[1]] = "←"

    def redraw_down_arrow(self, world):
        """
        If agent writes over the arrow when it moves through the world, this will redraw that arrow.
        """

        world[self.down_arrow[0]][self.down_arrow[1]] = "↓"

    def redraw_up_arrow(self, world):
        """
        If agent writes over the arrow when it moves through the world, this will redraw that arrow.
        """

        world[self.up_arrow[0]][self.up_arrow[1]] = "↑"

class Agent:

    def __init__(self, world):

        self.row = 1
        self.column = 1
        world[self.row][self.column]: list = "A"
        self.reward_pts = 0
        self.step_count = 0

    def out_of_bounds(self, direction: str) -> bool:
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

    def get_old_pos(self, direction: str) -> tuple[int, int]:
        """
        Depending on direction given, (north, south, east, west), the method can return the old position
        as tuple (row, column). This acts as a sensor used in the step methods, as this can help us determine
        if the previous position was on top of an arrow, so it can be given a reward.

        :param direction: direction we want to see the old position of: "north", "south", "east", or "west""
        :return: tuple of the previous position of the agent (row, column)
        """

        if direction == "north":
            return self.row - 1, self.column

        elif direction == "south":
            return self.row + 1, self.column

        elif direction == "east":
            return self.row, self.column + 1

        elif direction == "west":
            return self.row, self.column - 1

    def step_north(self, world, arrow: ArrowTiles) -> None:
        """
        Move the agent one cell to the north. If the agent will go out of bounds it will bounce back. If the
        previous position was any type of arrow, and the agent is travelling in the same direction that the
        arrow is pointing, it will be given a reward of 1 point

        :param world: final grid world
        :param arrow: ArrowTiles object, this is used to determine the position of the arrows to tell the agent
                      that it has passed an arrow
        :return: None
        """

        if self.out_of_bounds("north"):
            print("Out of bounds, bounce back")
            return

        # move agent
        self.row -= 1
        world[self.row][self.column] = "A"
        world[self.row + 1][self.column] = " "

        self.step_count += 1
        print(f"current step count = {self.step_count}")

        old_south = self.get_old_pos("south")

        # if cell to the south matches position of the up arrow, then the agent has move passed it, so gets a reward
        if old_south == arrow.up_arrow:
            self.reward_pts += 1
            arrow.redraw_up_arrow(world)

        # if the down arrow is the cell to south, then it needs to be redrawn, this is for cosmetic reasons
        elif old_south == arrow.down_arrow:
            arrow.redraw_down_arrow(world)

        print(f"reward points = {self.reward_pts}")

    def step_south(self, world, arrow: ArrowTiles) -> None:
        """
        Move the agent one cell to the south. If the agent will go out of bounds it will bounce back. If the
        previous position was any type of arrow, and the agent is travelling in the same direction that the
        arrow is pointing, it will be given a reward of 1 point

        :param world: final grid world
        :param arrow: ArrowTiles object, this is used to determine the position of the arrows to tell the agent
                      that it has passed an arrow
        :return: None
        """

        if self.out_of_bounds("south"):
            print("Out of bounds, bounce back")
            return

        # move agent
        self.row += 1
        world[self.row][self.column] = "A"
        world[self.row - 1][self.column] = " "

        self.step_count += 1

        old_north = self.get_old_pos("north")
        print(f"current step count = {self.step_count}")

        # if cell to the north matches position of the up arrow, then the agent has move passed it, so gets a reward
        if old_north == arrow.down_arrow:
            self.reward_pts += 1
            arrow.redraw_down_arrow(world)

        # if the up arrow is the cell to south, then it needs to be redrawn, this is for cosmetic reasons
        elif old_north == arrow.up_arrow:
            arrow.redraw_up_arrow(world)

        print(f"reward points = {self.reward_pts}")

    def step_east(self, world, arrow: ArrowTiles) -> None:
        """
        Move the agent one cell to the east. If the agent will go out of bounds it will bounce back. If the
        previous position was any type of arrow, and the agent is travelling in the same direction that the
        arrow is pointing, it will be given a reward of 1 point

        :param world: final grid world
        :param arrow: ArrowTiles object, this is used to determine the position of the arrows to tell the agent
                      that it has passed an arrow
        :return: None
        """

        if self.out_of_bounds("east"):
            print("Out of bounds, bounce back")
            return

        # move agent
        self.column += 1
        world[self.row][self.column] = "A"
        world[self.row][self.column - 1] = " "

        self.step_count += 1
        print(f"current step count = {self.step_count}")

        old_west = self.get_old_pos("west")

        # if cell to the west matches position of the up arrow, then the agent has move passed it, so gets a reward
        if old_west == arrow.right_arrow:
            self.reward_pts += 1
            arrow.redraw_right_arrow(world)

        # if the left arrow is the cell to south, then it needs to be redrawn, this is for cosmetic reasons
        elif old_west == arrow.left_arrow:
            arrow.redraw_left_arrow(world)

        print(f"reward points = {self.reward_pts}")

    def step_west(self, world, arrow: ArrowTiles) -> None:
        """
        Move the agent one cell to the west. If the agent will go out of bounds it will bounce back. If the
        previous position was any type of arrow, and the agent is travelling in the same direction that the
        arrow is pointing, it will be given a reward of 1 point

        :param world: final grid world
        :param arrow: ArrowTiles object, this is used to determine the position of the arrows to tell the agent
                      that it has passed an arrow
        :return: None
        """

        if self.out_of_bounds("west"):
            print("Out of bounds, bounce back")
            return

        # move agent
        self.column -= 1
        world[self.row][self.column] = "A"
        world[self.row][self.column + 1] = " "

        self.step_count += 1
        print(f"current step count = {self.step_count}")

        old_east = self.get_old_pos("east")

        # if cell to the east matches position of the up arrow, then the agent has move passed it, so gets a reward
        if old_east == arrow.left_arrow:
            self.reward_pts += 1
            arrow.redraw_left_arrow(world)

        # if the right arrow is the cell to south, then it needs to be redrawn, this is for cosmetic reasons
        elif old_east == arrow.right_arrow:
            arrow.redraw_right_arrow(world)

        print(f"reward points = {self.reward_pts}")
