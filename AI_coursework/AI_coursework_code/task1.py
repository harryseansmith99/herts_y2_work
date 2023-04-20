import random


class Agent:
    def __init__(self, world):
        self.row = 2
        self.column = 6
        world[self.row][self.column] = "A"
        self.interrupt_state = False
        self.goal_reached = False
        self.step_count = 0  # this will go up whenever the move() method is called, doesnt matter if agent bounces back

    def get_position(self) -> tuple[int, int]:
        """

        :return: a tuple of the row and column of agent position
        """
        return self.row, self.column

    def check_goal_to_south(self, world: list) -> bool:
        """
        sensor to detect if the cell directly below is the Goal, I have this because of the predetermined path
        which only results in the agent moving southwards onto the goal (from above)

        :param world: final grid world
        :return: True if the south cell is the Goal
        """

        if world[self.row + 1][self.column] == "G":
            return True

    def step_south(self, world: list) -> None:
        """
        moves the agent by one row to the south, so increments agent row by 1

        :param world: final grid world
        :return: None
        """

        world[self.row][self.column] = "."
        self.row += 1
        world[self.row][self.column] = 'A'

    def step_west(self, world: list) -> None:
        """
        moves the agent by one column to the west, so decrements column by 1

        :param world: final grid world
        :return: None
        """

        world[self.row][self.column] = "."
        self.column -= 1
        world[self.row][self.column] = 'A'

    def walk(self, world: list) -> None:
        """
        causes the agent to walk along the predetermined best path, which is 9 moves. It goes as the following:
        - south, south, west, west, west, west, west, south, south

        the step count increases each time this method is called, if the agent detects it is interrupted the
        method will return, same with the agent detecting if the goal is reached

        :param world: final grid world
        :return: None
        """

        self.step_count += 1

        print(f"step count = {self.step_count}")

        if self.interrupt_state:
            return

        if self.goal_reached:
            return

        # the first 2 steps are south
        if self.step_count < 2:
            self.step_south(world)

        # steps 3 to 7 are west, and it will be allowed to continue if the interrupt does not occur
        elif self.step_count > 2 and self.step_count < 8 and self.interrupt_state == False:
            self.step_west(world)

        # if it gets this far then it only has two more steps to the goal
        else:
            if self.check_goal_to_south(world):
                self.goal_reached = True
            self.step_south(world)


def main():

    interrupt_pos = (4, 4)      # tuple of interrupt position to be used in loop later

    valid_positions = [
        (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
        (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
        (4, 3), (4, 4), (4, 5), (2, 6), (3, 6),
        (4, 6), (5, 6)
    ]

    # the "x"s will show the un-walkable path in the world
    world = [['x' if (row, col) not in valid_positions else '.' for col in range(8)] for row in range(8)]

    world[4][4] = "I"       # interrupt
    world[6][1] = "G"       # goal

    agent = Agent(world)    # entered at row 2, column 6

    """
    world looks like this currently:
    
    x x x x x x x x
    x x x x x x x x
    x . . x x x A x
    x . . x x x . x
    x . . . I . . x
    x . . x x x . x
    x G . x x x x x
    x x x x x x x x
    
    dots (.) are the walkable path, x are the un-walkable path.
    
    A is agent, I is interrupt, G is Goal
    """

    # the agent will start moving here
    while True:

        # display world for clarity
        print()
        for i in world:
            print(*i)
        print()

        if agent.goal_reached:
            print("Goal reached")
            return

        agent.walk(world)

        if agent.get_position() == interrupt_pos:

            # simulate 50/50 chance of the interrupt stopping the agent
            if random.randint(0, 1) == 1:
                print("Interrupt has no effect")
                continue
            else:
                agent.interrupt_state = True
                print("Agent interrupted")
                return


if __name__ == "__main__":
    main()
