import pygame

import doska


def draw_border():
    for x in range(0, doska.field_width):
        doska.putObject(x, 0, doska.CellType.Zabor)
        doska.putObject(x, doska.field_height - 1, doska.CellType.Zabor)

    for y in range(0, doska.field_height):
        doska.putObject(0, y, doska.CellType.Zabor)
        doska.putObject(doska.field_width - 1, y, doska.CellType.Zabor)
