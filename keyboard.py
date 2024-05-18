import turtle

import doska


def go_up():
    doska.vy = 1
    doska.vx = 0


def go_down():
    doska.vy = -1
    doska.vx = 0


def go_left():
    doska.vy = 0
    doska.vx = -1


def go_right():
    doska.vy = 0
    doska.vx = 1
def setup_keyboard():
    # keyboard settings
    screen = turtle.Screen()
    screen.onkeypress(go_up, "w")
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")
    # screen.onkeypress(go_up, "ц")
    # screen.onkeypress(go_down, "ы")
    # screen.onkeypress(go_left, "ф")
    # screen.onkeypress(go_right, "в")
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")
    screen.onkeypress(go_right, "Right")
    screen.listen()