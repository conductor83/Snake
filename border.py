import turtle
import doska


def draw_border():
    border = turtle.Turtle()
    border.shape("turtle")  # turtle
    border.penup()
    border.color("white")

    for x in range(0,doska.field_width):
        border.goto(doska.calc_gx(x), doska.calc_gy(0))
        border.stamp()
        border.goto(doska.calc_gx(x), doska.calc_gy(doska.field_height-1))
        border.stamp()

    for y in range(0,doska.field_height):
        border.goto(doska.calc_gx(0), doska.calc_gy(y))
        border.setheading(180)
        border.stamp()
        border.goto(doska.calc_gx(doska.field_width-1), doska.calc_gy(y))
        border.setheading(0)
        border.stamp()

