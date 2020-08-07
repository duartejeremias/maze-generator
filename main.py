# Created by: Duarte Jeremias

from classes import Maze, Position
from interface import ui, SCREEN


def main(width, length, density, method):
    maze = Maze(length, width)  # maze creation (Start and End point generated)
    if method == 'FAST':
        solution = maze.path_find()  # checking if maze is possible
        maze.mk_walls(density)  # wall creation
    else:
        maze.mk_walls(density)  # wall creation
        solution = maze.path_find()  # checking if maze is possible

        # if not possible
        while not solution:  # loop until a possible maze is generated
            maze.walls.clear()  # clears previous generation's walls
            maze.mk_walls(density)  # generates new wall's
            solution = maze.path_find()  # checks if new maze is possible
    print(maze)

    ui(SCREEN, length, width, maze)


width = int(input("Enter a width (integer): "))
length = int(input("Enter a length (integer): "))
density = float(input("Enter a wall density (0-100 percentage): "))
method = input("Enter 'FAST' for fast generation (first path then walls) or 'SLOW' for slow generation (first walls then path: ")
density = density / 100


main(width, length, density, method)
