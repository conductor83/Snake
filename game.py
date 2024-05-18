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
    if globals.x==-1 or globals.x == globals.field_width:
        return True
    if globals.y == -1 or globals.y == globals.field_height:
        return True


    return False

def start_game():
    # Set up the screen
    screen = turtle.Screen()

    screen.title("Snake Game by Katya")

    screen.bgcolor("green")
    screen.setup(width=globals.yacheika_size * (globals.field_width) - globals.yacheika_size // 2, height=globals.yacheika_size * (globals.field_height) - globals.yacheika_size // 2)
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
        head.goto(globals.calc_gx(globals.x),globals.calc_gy(globals.y))

        # ждем секунду
        time.sleep(0.3)

    screen.mainloop()
