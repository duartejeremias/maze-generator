import pygame
from math import sqrt
from classes import Position, Maze

SCREEN_WIDTH = 1080
SCREEN_LENGTH = 1920

SCREEN = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
pygame.display.set_caption("Random Maze Generator")

WHITE = (255, 255, 255)  # free space color
BLACK = (0, 0, 0)  # wall space color
RED = (255, 0, 0)  # end position color
BLUE = (0, 0, 255)  # start position color
YELLOW = (253, 185, 0)  # path color
GREY = (128, 128, 128)  # line color


class Spot:
    def __init__(self, position, width):
        self.position = position  # maze position
        self.width = width  # width of each spot
        self.x = position.x * width  # collumn position on UI
        self.y = position.y * width  # row position on UI
        self.color = WHITE

    def get_position(self):
        return self.x, self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))


def mk_grid(width, length, maze):
    grid = []
    gap = sqrt(pow(SCREEN_WIDTH, 2) // (width * length))
    for i in range(width):
        grid.append([])
        for j in range(length):
            pos = Position(j, i)
            spot = Spot(pos, gap)
            if pos in maze.walls:
                spot.color = BLACK
            elif pos == maze.start:
                spot.color = BLUE
            elif pos == maze.end:
                spot.color = RED
            elif pos in maze.path:
                spot.color = YELLOW

            grid[i].append(spot)

    return grid


def draw_grid(screen, width, length):
    gap = sqrt(pow(SCREEN_WIDTH, 2) // (width * length))
    for i in range(1, width):
        pygame.draw.line(screen, GREY, (0, i * gap), (length * gap, i * gap))
        for j in range(1, length):
            pygame.draw.line(screen, GREY, (j * gap, 0), (j * gap, width * gap))


def draw(screen, grid, width, length):
    screen.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(screen)

    draw_grid(screen, width, length)
    pygame.display.update()


def ui(screen, length, width, maze):
    pygame.init()
    grid = mk_grid(width, length, maze)

    run = True

    draw(screen, grid, width, length)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


