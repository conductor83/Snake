import turtle
import time
import random

sprite_size = 16  # pixel
field_height = 40  # cells
field_width = 40  # cells

x = field_height // 2
y = field_width // 2
vx = 0
vy = 0


def move():
    global x
    global y

    x = x + vx
    y = y + vy


# Functions
def go_up():
    global vy, vx
    vy = 1
    vx = 0


def go_down():
    global vy, vx
    vy = -1
    vx = 0


def go_left():
    global vy, vx
    vy = 0
    vx = -1


def go_right():
    global vy, vx
    vy = 0
    vx = 1


def check_gameover():
    global x, y
    global field_width, field_height

    return False


def start_game():
    global x
    global y

    # Set up the screen
    screen = turtle.Screen()

    screen.title("Snake Game by @TokyoEdTech")

    screen.bgcolor("green")
    screen.setup(width=sprite_size * field_width, height=sprite_size * field_height)
    screen.tracer(0)  # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.shape("circle")  # turtle
    head.penup()
    head.color("red")

    screen.onkeypress(go_up, "w")
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")
    screen.listen()

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
        head.goto((x - field_width // 2) * sprite_size,
                  (y - field_height // 2) * sprite_size)

        # ждем секунду
        time.sleep(1)

    screen.mainloop()
