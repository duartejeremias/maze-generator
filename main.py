# Created by: Duarte Jeremias

from random import randrange


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_outer_wall(self, length, width):
        """
        returns the bool value depending on if the position is in the outer wall or not
        :param length:
        :param width:
        :return:
        """
        if self.x == length - 1 or self.y == width - 1 or self.x == 0 or self.y == 0:
            return True
        return False

    def is_corner(self, length, width):
        """
        returns the bool value depending on if the position is a corner or not
        :param length:
        :param width:
        :return:
        """
        if (self.x == 0 and self.y == 0) or (self.x == length - 1 and self.y == width - 1) or \
                (self.x == 0 and self.y == width - 1) or (self.x == length - 1 and self.y == 0):
            return True
        return False


class Maze:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        self.outer_walls = []  # array with the positions of every outer wall
        size = 0
        for y in range(0, width):
            for x in range(0, length):
                pos = Position(x, y)
                if pos.is_outer_wall(length, width):
                    pos.is_wall = True
                    self.outer_walls.append(pos)
                    size += 1

        self.inner_walls = []  # array with the positions of every inner wall
        self.path = []  # array with the positions of the path taken

        # generating a start point
        index = randrange(size)
        # loop while the point generated is in the corner
        while self.outer_walls[index].is_corner(length, width):
            index = randrange(size)
        self.start = self.outer_walls[index]

        # generating an end point
        index = randrange(size)
        # loop while the point generated is in the same wall or collumn as start point or in the corner
        while self.outer_walls[index].is_corner(length, width) or self.outer_walls[index].x == self.start.x or \
                self.outer_walls[index].y == self.start.y:
            index = randrange(size)
        self.end = self.outer_walls[index]

    def __str__(self):
        result = ""
        for i in range(0, self.width):
            for j in range(0, self.length):
                pos = Position(j, i)
                if pos == self.start:
                    result += "S"
                elif pos == self.end:
                    result += "E"
                elif pos in self.outer_walls or pos in self.inner_walls:
                    result += "#"
                else:
                    result += "."
            result += "\n"
        return result[:-1]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end


width = 5
length = 10
maze = Maze(length, width)
print(maze.start)
print(maze.end)
print(maze)
