from random import randrange
from math import sqrt


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # variables for use in path-finding algorithm
        self.f = 0  # g and h added
        self.g = 0  # distance to start point
        self.h = 0  # distance to end point
        self.parent = None  # parent position

    def __repr__(self):
        return self.x, self.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def calculte_f(self, start, end):
        """
        returns the f cost of the given position
        :param start (start position):
        :param end (end position):
        :return:
        """
        if self == start:
            return 0
        self.g = sqrt(pow(start.x - self.x, 2) + pow(start.y - self.y, 2))
        self.h = sqrt(pow(end.x - self.x, 2) + pow(end.y - self.y, 2))
        self.f = self.g + self.h


class Maze:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        self.walls = []  # array with the positions of every wall
        self.path = []  # array with the positions of the path taken

        # generating a start point
        self.start = Position(randrange(length), randrange(width))

        # generating an end point
        x = randrange(length)
        y = randrange(width)
        # loop while the point generated is in the same wall or collumn as start point
        while x == self.start.x or y == self.start.y:
            x = randrange(length)
            y = randrange(width)
        self.end = Position(x, y)

    def __str__(self):
        result = ""
        for i in range(0, self.width):
            for j in range(0, self.length):
                pos = Position(j, i)
                if pos == self.start:
                    result += "S"
                elif pos == self.end:
                    result += "E"
                elif pos in self.walls:
                    result += "#"
                elif pos in self.path:
                    result += "="
                else:
                    result += "."
            result += "\n"
        return result[:-1]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def mk_walls(self, density):
        """
        generates the walls of the maze
        :param density:
        :return:
        """
        if not isinstance(density, float) or density < 0 or density > 1.0:
            raise ValueError("Density must be a float between 0 and 1.0")

        num_walls = int(((self.width * self.length) - 2) * density)  # calculating number of walls

        while num_walls != 0:
            x = randrange(self.length)
            y = randrange(self.width)
            pos = Position(x, y)
            if (pos in self.walls) or (pos in self.path) or pos == self.start or pos == self.end:
                continue
            else:
                self.walls.append(pos)
                num_walls -= 1

    def path_find(self):
        """
        method that calculates maze's solution
        :return: false if no solution, true otherwise
        """

        # initialize both open and closed lists
        open_list = [self.start]  # list that contains positions to be processed
        closed_list = []  # list that contains processed positions

        # main function loop
        while len(open_list) > 0:

            # gets current position (position to process)
            current_pos = open_list[0]
            current_index = 0
            for i, pos in enumerate(open_list):
                if pos.f < current_pos.f:
                    current_pos = pos
                    current_index = i

            open_list.pop(current_index)  # removes current position from open list
            closed_list.append(current_pos)  # inserts current position into closed list (is going to be processed)

            # end found
            if current_pos == self.end:
                current = current_pos
                # backtracks to origin
                while current is not None:
                    self.path.append(current)
                    current = current.parent

                self.path = self.path[::-1]  # reverts path order
                return True

            # generate children (positions adjacent to current position)
            children = []
            for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                # generate position
                node_pos = Position(current_pos.x + new_pos[0], current_pos.y + new_pos[1])

                # makes sure new position is inside the maze's boundaries
                if node_pos.x > (self.length - 1) or node_pos.x < 0 or node_pos.y >(self.width - 1) or node_pos.y < 0:
                    continue

                # makes sure new position hasn't been checked to avoid infinite loops
                if node_pos in closed_list:
                    continue

                # makes sure new position isn't a maze wall
                if node_pos in self.walls:
                    continue

                node_pos.parent = current_pos  # update to the position parent
                children.append(node_pos)  # appends to the available children

            # loop through the children
            for child in children:

                child.calculte_f(self.start, self.end)  # f cost calculation

                # loop to see if child is in open list
                for open_child in open_list:
                    if child == open_child and child.g > open_child.g:
                        continue

                open_list.append(child)  # add child to open list

        self.path.clear()  # if no path calculated, clear the path and return false
        return False
