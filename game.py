import time
import pygame
import doska
from border import draw_border
from keyboard import process_key


def move():
    doska.x = doska.x + doska.vx
    doska.y = doska.y + doska.vy


# Functions

def check_gameover():
    if doska.x == 0 or doska.x == doska.field_width-1:
        return True
    if doska.y == 0 or doska.y == doska.field_height-1:
        return True

    return False


def start_game():

    clock = pygame.time.Clock()

    doska.game_window.fill("green")

    draw_border()

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

        # поменяли вид экрана
        doska.putObject(doska.x, doska.y, doska.CellType.Head)


        # Refresh game screen
        pygame.display.update()

        # проверили, что игра продолжается
        game_over = check_gameover()
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

        clock.tick(2)  # limits FPS

    pygame.quit()
