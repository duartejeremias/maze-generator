# Created by: Duarte Jeremias

from random import randrange
from math import sqrt


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None

    def __repr__(self):
        return self.x, self.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


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
            if (pos in self.walls) or pos == self.start or pos == self.end:
                continue
            else:
                self.walls.append(pos)
                num_walls -= 1


def calculte_f(pos, start, end):
    if pos == start:
        return 0
    pos.g = sqrt(pow(start.x - pos.x, 2) + pow(start.y - pos.y, 2))
    pos.h = sqrt(pow(end.x - pos.x, 2) + pow(end.y - pos.y, 2))
    return pos.g + pos.h


def path_find(maze):
    open_list = [maze.start]
    closed_list = []

    while len(open_list) > 0:
        current_pos = open_list[0]
        current_index = 0
        for i, pos in enumerate(open_list):
            if pos.f < current_pos.f:
                current_pos = pos
                current_index = i

        open_list.pop(current_index)
        closed_list.append(current_pos)

        if current_pos == maze.end:
            current = current_pos
            while current is not None:
                maze.path.append(current)
                current = current.parent
            return True

        children = []
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_pos = Position(current_pos.x + new_pos[0], current_pos.y + new_pos[1])

            if node_pos.x > (maze.length - 1) or node_pos.x < 0 or node_pos.y >(maze.width - 1) or node_pos.y < 0:
                continue

            if node_pos in closed_list:
                continue

            if node_pos in maze.walls:
                continue

            node_pos.parent = current_pos
            children.append(node_pos)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.f = calculte_f(child, maze.start, maze.end)

            for open_child in open_list:
                if child == open_child and child.g > open_child.g:
                    continue

            open_list.append(child)
    maze.path.clear()
    return False

width = 32
length = 64
density = 0.2


def run(width, length, density):
    maze = Maze(length, width)
    maze.mk_walls(density)
    solution = False
    while not solution:
        solution = path_find(maze)
    print(maze)


run(width, length, density)