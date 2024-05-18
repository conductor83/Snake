import turtle
import globals


def draw_border():
    border = turtle.Turtle()
    border.shape("turtle")  # turtle
    border.penup()
    border.color("white")

    for x in range(0,globals.field_width):
        border.goto(globals.calc_gx(x), globals.calc_gy(0))
        border.stamp()
        border.goto(globals.calc_gx(x), globals.calc_gy(globals.field_height-1))
        border.stamp()

    for y in range(0,globals.field_height):
        border.goto(globals.calc_gx(0), globals.calc_gy(y))
        border.setheading(180)
        border.stamp()
        border.goto(globals.calc_gx(globals.field_width-1), globals.calc_gy(y))
        border.setheading(0)
        border.stamp()

