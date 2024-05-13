import turtle
import time
import random
import globals
from border import draw_border

def move():
    globals.x = globals.x + globals.vx
    globals.y = globals.y + globals.vy


# Functions
def go_up():
    globals.vy = 1
    globals.vx = 0


def go_down():
    globals.vy = -1
    globals.vx = 0


def go_left():
    globals.vy = 0
    globals.vx = -1


def go_right():
    globals.vy = 0
    globals.vx = 1


def check_gameover():
    ## x, y
    # field_width, field_height

    return False

def start_game():
    # Set up the screen
    screen = turtle.Screen()

    screen.title("Snake Game by Katya")

    screen.bgcolor("green")
    screen.setup(width=globals.sprite_size * (globals.field_width)-globals.sprite_size//2, height=globals.sprite_size * (globals.field_height)-globals.sprite_size//2)
    screen.tracer(0)  # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.shape("circle")  # turtle
    head.penup()
    head.color("red")

    # keyboard settings
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

    draw_border()

    while True:
        # дали экрану нарисовать себя, а клавишщам сработать
        screen.update()

        ## посчитали
        move()

        # проерили, что игра продолжается
        game_over = check_gameover()
        if game_over:
            message = turtle.Turtle()
            message.color("white")
            message.penup()
            message.hideturtle()
            message.goto(0, 0)
            message.write("Game OVER", font=("Arial", 28, "normal"))

            screen.mainloop()
            return

        # поменяли вид экрана
        head.goto(globals.calc_gx(globals.x),globals.calc_gy(globals.y))

        # ждем секунду
        time.sleep(1)

    screen.mainloop()
