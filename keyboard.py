import pygame

import body
import doska


def go_up():
    body.vy = 1
    body.vx = 0


def go_down():
    body.vy = -1
    body.vx = 0


def go_left():
    body.vy = 0
    body.vx = -1


def go_right():
    body.vy = 0
    body.vx = 1


def process_key(key):
    if key == pygame.K_UP or key == pygame.K_w:
        go_up()
    if key == pygame.K_DOWN or key == pygame.K_s:
        go_down()
    if key == pygame.K_LEFT or key == pygame.K_a:
        go_left()
    if key == pygame.K_RIGHT or key == pygame.K_d:
        go_right()
