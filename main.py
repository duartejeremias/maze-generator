# Created by: Duarte Jeremias

from classes import Maze, Position

width = 5
length = 10
density = 0.9


def main(width, length, density):
    maze = Maze(length, width)  # maze creation (Start and End point generated)

    maze.mk_walls(density)  # wall creation
    solution = maze.path_find()  # checking if maze is possible

    # if not possible
    while not solution:  # loop until a possible maze is generated
        maze.walls.clear()  # clears previous generation's walls
        maze.mk_walls(density)  # generates new wall's
        solution = maze.path_find()  # checks if new maze is possible
    print(maze)


main(width, length, density)

