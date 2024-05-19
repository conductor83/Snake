import pygame

import doska


def draw_border(game_window):
    for x in range(0, doska.field_width):
        pygame.draw.circle(game_window, "white", doska.calc_gpos(x, 0), doska.yacheika_size / 2)
        pygame.draw.circle(game_window, "white", doska.calc_gpos(x, doska.field_height - 1),
                           doska.yacheika_size / 2)

    for y in range(0, doska.field_height):
        pygame.draw.circle(game_window, "white", doska.calc_gpos(0, y), doska.yacheika_size / 2)
        pygame.draw.circle(game_window, "white", doska.calc_gpos(doska.field_width - 1, y),
                           doska.yacheika_size / 2)
