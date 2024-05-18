import turtle
import time
import random
import doska
from border import draw_border
from keyboard import setup_keyboard


def move():
    doska.x = doska.x + doska.vx
    doska.y = doska.y + doska.vy


# Functions



def check_gameover():
    if doska.x==-1 or doska.x == doska.field_width:
        return True
    if doska.y == -1 or doska.y == doska.field_height:
        return True


    return False

def start_game():
    # Set up the screen
    screen = turtle.Screen()

    screen.title("Snake Game by Katya")

    screen.bgcolor("green")
    screen.setup(width=doska.yacheika_size * (doska.field_width) - doska.yacheika_size // 2, height=doska.yacheika_size * (doska.field_height) - doska.yacheika_size // 2)
    screen.tracer(0)  # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.shape("circle")  # turtle
    head.penup()
    head.color("red")

    setup_keyboard()

    draw_border()

    while True:
        # дали экрану нарисовать себя, а клавишщам сработать
        screen.update()

        ## посчитали
        move()

        # проерили, что игра продолжается
        game_over = check_gameover()
        if game_over:
            time.sleep(1)
            message = turtle.Turtle()
            message.color("white")
            message.penup()
            message.hideturtle()
            message.goto(0, 0)
            message.write("Game OVER", font=("Arial", 28, "normal"))

            screen.mainloop()
            return

        # поменяли вид экрана
        head.goto(doska.calc_gx(doska.x),doska.calc_gy(doska.y))

        # ждем секунду
        time.sleep(0.3)

    screen.mainloop()
