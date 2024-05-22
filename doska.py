from enum import Enum

import pygame

yacheika_size = 16  # pixel

field_height = 25  # cells
field_width = 25  # cells



window_size_x = yacheika_size * (field_width - 1)
window_size_y = yacheika_size * (field_height - 1)

pygame.init()

# Set up the screen
pygame.display.set_caption('Snake Game by Katya')
game_window = pygame.display.set_mode((window_size_x, window_size_y))


class CellType(Enum):
    Empty = 0
    Zabor = 1
    Head = 2
    Body = 3
    Rabbit = 4


field = [[CellType.Empty] * field_width for i in range(field_height)]


def putObject(x: int, y: int, celltype: CellType):
    if x < 0 or x > field_width-1:
        raise Exception("Неверная координата х")
    if y < 0 or y > field_height-1:
        raise Exception("Неверная координата y")
    field[x][y] = celltype

    match celltype:
        case CellType.Empty:
            pygame.draw.circle(game_window, "green", calc_gpos(x, y), yacheika_size / 2)
        case CellType.Zabor:
            pygame.draw.circle(game_window, "white", calc_gpos(x, y), yacheika_size / 2)
        case CellType.Head:
            pygame.draw.circle(game_window, "red", calc_gpos(x, y), yacheika_size / 2)
        case CellType.Body:
            pygame.draw.circle(game_window, "orange", calc_gpos(x, y), yacheika_size / 2)
        case CellType.Rabbit:
            pygame.draw.circle(game_window, "gray", calc_gpos(x, y), yacheika_size / 2)


def calc_gx(doska_x):
    return doska_x * yacheika_size


def calc_gy(doska_y):
    return window_size_y - doska_y * yacheika_size


def calc_gpos(doska_x, doska_y):
    return calc_gx(doska_x), calc_gy(doska_y)
