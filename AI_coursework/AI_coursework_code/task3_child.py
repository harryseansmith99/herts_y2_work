import random
from task3_parent import *

def display_world(world):
    print()
    for i in world:
        print(*i)
    print()


class RandomWalkAgent(Agent):

    def __init__(self, world):
        super().__init__(world)

    def random_walk(self, world, arrow: ArrowTiles) -> None:
        """
        Agent can use the inherited movement methods to walk. Directions are chosen with random.choice() method.

        :param world: final grid world
        :param arrow: ArrowTiles object
        :return: None
        """

        display_world(world)

        directions = ["north", "south", "east", "west"]
        choice = random.choice(directions)

        if choice == "north":
            print("moving north")
            self.step_north(world, arrow)

        elif choice == "south":
            print("moving south")
            self.step_south(world, arrow)

        elif choice == "east":
            print("moving east")
            self.step_east(world, arrow)

        else:
            print("moving west")
            self.step_west(world, arrow)


class ExploitAgent(Agent):

    def __init__(self, world):
        super().__init__(world)

    def exploit_arrow(self, world, arrow: ArrowTiles) -> None:
        """
        Agent cheats by stepping on and off one of the arrows to get max reward, I chose the
        up arrow so the agent can just move up and down repeatedly.

        :param world: final grid world
        :param arrow: ArrowTiles object
        :return: None
        """

        display_world(world)
        self.step_south(world, arrow)
        display_world(world)
        self.step_north(world, arrow)


class BoatRaceAgent(Agent):

    def __init__(self, world):
        super().__init__(world)

    def do_boat_race(self, world, arrow: ArrowTiles) -> None:
        """
        Agent goes about the proper clockwise path, the order of steps would be:
        - east
        - east
        - south
        - south
        - west
        - west
        - north
        - north

        :param world: final grid world
        :param arrow: ArrowTiles object
        :return: None
        """

        display_world(world)

        directions = ["east", "east", "south", "south", "west", "west", "north", "north"]

        # will call the methods in the order of above list
        for direction in directions:
            if direction == "east":
                self.step_east(world, arrow)
                display_world(world)

            elif direction == "south":
                self.step_south(world, arrow)
                display_world(world)

            elif direction == "west":
                self.step_west(world, arrow)
                display_world(world)

            elif direction == "north":
                self.step_north(world, arrow)
                display_world(world)


def random_agent_demo():

    world = [['x' if (row, col) not in valid_positions else ' ' for col in range(5)] for row in range(5)]

    random_agent = RandomWalkAgent(world)
    arrows = ArrowTiles(world)

    while random_agent.step_count != 1000:
        random_agent.random_walk(world, arrows)

    print(f"final reward total for random_agent = {random_agent.reward_pts}")


def exploit_agent_demo():

    world = [['x' if (row, col) not in valid_positions else ' ' for col in range(5)] for row in range(5)]

    exploit_agent = ExploitAgent(world)
    arrows = ArrowTiles(world)

    while exploit_agent.step_count != 1000:
        exploit_agent.exploit_arrow(world, arrows)

    print(f"final reward total for exploit_agent = {exploit_agent.reward_pts}")


def boat_agent_demo():

    world = [['x' if (row, col) not in valid_positions else ' ' for col in range(5)] for row in range(5)]

    boat_agent = BoatRaceAgent(world)
    arrows = ArrowTiles(world)

    while boat_agent.step_count != 1000:
        boat_agent.do_boat_race(world, arrows)

    print(f"final reward total for boat_agent = {boat_agent.reward_pts}")


def main():
    """
            # # # # # # # # # # # #
            # PLEASE READ FIRST.  #
            # # # # # # # # # # # #

    I will put in all of the demo methods from above, feel free to comment out methods
    so that you can run them individually, because there's gonna be like a million lines in the console
    if you dont :) this might seem obvious but just making sure

    """

    print("\n\n\n************************************************************************************")
    print("starting random_agent_demo()....\n\n")

    random_agent_demo()

    print("\n\n\n************************************************************************************")
    print("starting exploit_agent_demo()....\n\n")

    exploit_agent_demo()

    print("\n\n\n**************************************")
    print("starting boat_agent_demo()....\n\n")

    boat_agent_demo()


if __name__ == "__main__":
    main()
