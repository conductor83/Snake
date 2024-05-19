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
    if doska.x == -1 or doska.x == doska.field_width:
        return True
    if doska.y == -1 or doska.y == doska.field_height:
        return True

    return False


def start_game():
    pygame.init()

    # Set up the screen
    pygame.display.set_caption('Snake Game by Katya')
    game_window = pygame.display.set_mode((doska.window_size_x, doska.window_size_y))
    clock = pygame.time.Clock()

    game_window.fill("green")

    draw_border(game_window)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                process_key(event.key)

        #стираем голову в старом месте
        pygame.draw.circle(game_window, "green", doska.calc_gpos(doska.x, doska.y), doska.yacheika_size / 2)

        ## посчитали новое положение головы
        move()

        # проверили, что игра продолжается
        game_over = check_gameover()
        if game_over:
            time.sleep(1)

            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render('Game OVER', True, 'red')
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (doska.window_size_x / 2, doska.window_size_y / 4)
            game_window.blit(game_over_surface, game_over_rect)

            pygame.display.flip()

            time.sleep(3)
            running = False

        # поменяли вид экрана
        pygame.draw.circle(game_window, "red", doska.calc_gpos(doska.x, doska.y), doska.yacheika_size/2)

        # Refresh game screen
        pygame.display.update()

        clock.tick(2)  # limits FPS

    pygame.quit()
