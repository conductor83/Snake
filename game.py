import time
from random import random, randint

import pygame
import doska
import body
from border import draw_border
from keyboard import process_key


def move():
    if body.vx == 0 and body.vy ==0:
        return False

    x,y = body.body_arr[body.head_idx]

    new_x = x + body.vx
    new_y = y + body.vy

    game_over = check_gameover(new_x,new_y)
    
    if game_over:
        return game_over
    
    body.head_idx = body.head_idx+1
    if body.head_idx == len(body.body_arr):
        body.head_idx =0
        
    body.body_arr[body.head_idx] = (new_x, new_y)
    #заменяем изображение головы на изображение тела
    doska.putObject(x, y, doska.CellType.Body)
    # нарисовали новую голову
    doska.putObject(new_x, new_y, doska.CellType.Head)
    
    if body.grow==0:
        tx,ty = body.body_arr[body.tail_idx]
        #стираем последний элемент хвоста
        doska.putObject(tx,ty, doska.CellType.Empty)
    
        body.tail_idx = body.tail_idx + 1
        if body.tail_idx == len(body.body_arr):
            body.tail_idx = 0
    else:
        if body.head_idx>body.tail_idx:
            len_snake = body.head_idx - body.tail_idx+1
            if len_snake == len(body.body_arr):
                body.body_arr = body.body_arr+[None]*len(body.body_arr)
        else:
            len_snake = len(body.body_arr)-(body.tail_idx - body.head_idx)+1
            if len_snake == len(body.body_arr):
                body.body_arr = body.body_arr[body.tail_idx:] + body.body_arr[:body.head_idx+1]+[None]*len(body.body_arr)
                body.tail_idx = 0
                body.head_idx = len_snake-1

        body.grow = body.grow-1




# Functions

def check_gameover(x,y):
    celltype = doska.field[x][y]

    match celltype:
        case doska.CellType.Zabor:
           return True
        case doska.CellType.Head:
            raise Exception("Какая-то шняга с головой")
        case doska.CellType.Body:
            return True
        case doska.CellType.Rabbit:
            body.grow = body.grow+3
            while True:
                rx= randint(1,doska.field_width-2)
                ry=randint(1,doska.field_height-2)
                if doska.field[rx][ry] ==doska.CellType.Empty:
                    doska.putObject(rx,ry,doska.CellType.Rabbit)
                    break
        case _: #то же, что else
            return False



def start_game():

    clock = pygame.time.Clock()

    doska.game_window.fill("green")

    draw_border()

    doska.putObject(9,10,doska.CellType.Rabbit)
    doska.putObject(3, 5, doska.CellType.Rabbit)

    x, y = body.body_arr[body.head_idx]
    doska.putObject(x, y, doska.CellType.Head)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                process_key(event.key)

        game_over = move()

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

        fps = min(30, body.calc_snake_len()//10+1)
        clock.tick(fps)  # limits FPS

    pygame.quit()
