import time
from random import random, randint

import pygame
import doska
from border import draw_border
from keyboard import process_key


def move():
    doska.x = doska.x + doska.vx
    doska.y = doska.y + doska.vy


# Functions

def check_gameover():
    celltype = doska.field[doska.x][doska.y]

    match celltype:
        case doska.CellType.Zabor:
           return True
        case doska.CellType.Head:
            raise Exception("Какая-то шняга с головой")
        case doska.CellType.Body:
            return True
        case doska.CellType.Rabbit:
            while True:
                x= randint(1,doska.field_width-2)
                y=randint(1,doska.field_height-2)
                if doska.field[x][y] ==doska.CellType.Empty:
                    doska.putObject(x,y,doska.CellType.Rabbit)
                    break
        case _: #то же, что else
            return False



def start_game():

    clock = pygame.time.Clock()

    doska.game_window.fill("green")

    draw_border()

    doska.putObject(9,10,doska.CellType.Rabbit)
    doska.putObject(3, 5, doska.CellType.Rabbit)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                process_key(event.key)

        #стираем голову в старом месте
        doska.putObject(doska.x,doska.y, doska.CellType.Empty)

        ## посчитали новое положение головы
        move()

        # проверили, что игра продолжается
        game_over = check_gameover()

        # поменяли вид экрана
        doska.putObject(doska.x, doska.y, doska.CellType.Head)



        # Refresh game screen
        pygame.display.update()

        if game_over:
            time.sleep(1)

            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render('Game OVER', True, 'red')
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (doska.window_size_x / 2, doska.window_size_y / 4)
            doska.game_window.blit(game_over_surface, game_over_rect)

            pygame.display.flip()

            time.sleep(3)
            running = False

        clock.tick(4)  # limits FPS

    pygame.quit()
