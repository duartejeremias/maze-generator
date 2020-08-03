# Created by: Duarte Jeremias

from random import randrange


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.x, self.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_border(self, length, width):
        """
        returns the bool value depending on if the position is on the border or not
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

        self.border = []  # array with the positions of border positions
        size = 0
        for y in range(0, width):
            for x in range(0, length):
                pos = Position(x, y)
                if pos.is_border(length, width):
                    self.border.append(pos)
                    size += 1

        self.walls = []  # array with the positions of every wall
        self.path = []  # array with the positions of the path taken

        # generating a start point
        index = randrange(size)
        # loop while the point generated is in the corner
        while self.border[index].is_corner(length, width):
            index = randrange(size)
        self.start = self.border[index]

        # generating an end point
        index = randrange(size)
        # loop while the point generated is in the same wall or collumn as start point or in the corner
        while self.border[index].is_corner(length, width) or self.border[index].x == self.start.x or \
                self.border[index].y == self.start.y:
            index = randrange(size)
        self.end = self.border[index]

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
                else:
                    result += "."
            result += "\n"
        return result[:-1]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def mk_walls(self, density):
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


width = 5
length = 10
density = 0.5


def run(width, length, density):
    maze = Maze(length, width)
    maze.mk_walls(density)
    print(maze.start)
    print(maze.end)
    print(maze)


run(width, length, density)