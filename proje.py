
import turtle

screen = turtle.Screen()
screen.setup(900, 650)
screen.title("Mountain Cabin")
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()

    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.end_fill()


def draw_triangle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()

    pen.goto(x + size / 2, y + size)
    pen.goto(x + size, y)
    pen.goto(x, y)

    pen.end_fill()


def draw_circle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()


draw_circle(250, 180, 55, "yellow")

draw_triangle(-450, -80, 400, "gray")
draw_triangle(-200, -80, 450, "darkgray")
draw_triangle(100, -80, 400, "dimgray")

draw_triangle(-320, 190, 140, "white")
draw_triangle(-50, 230, 150, "white")
draw_triangle(230, 190, 140, "white")

draw_rectangle(-450, -325, 900, 180, "skyblue")
draw_rectangle(-450, -145, 900, 65, "forestgreen")


def draw_tree(x, y):
    draw_rectangle(x + 25, y, 20, 70, "brown")
    draw_triangle(x, y + 40, 70, "darkgreen")
    draw_triangle(x + 5, y + 70, 60, "green")
    draw_triangle(x + 10, y + 100, 50, "darkgreen")


draw_tree(-400, -145)
draw_tree(-310, -145)
draw_tree(300, -145)
draw_tree(380, -145)


def draw_cabin():
    draw_rectangle(-120, -145, 240, 150, "saddlebrown")

    pen.color("black")

    for y in range(-120, 5, 25):
        pen.penup()
        pen.goto(-120, y)
        pen.pendown()
        pen.goto(120, y)

    draw_triangle(-150, 5, 300, "maroon")

    draw_rectangle(-30, -145, 60, 100, "brown")

    draw_circle(15, -100, 5, "yellow")

    draw_rectangle(-100, -65, 50, 50, "lightyellow")
    draw_rectangle(50, -65, 50, 50, "lightyellow")

    pen.color("black")

    for x in [-75, 75]:
        pen.penup()
        pen.goto(x, -65)
        pen.pendown()
        pen.goto(x, -15)

        pen.penup()
        pen.goto(x - 25, -40)
        pen.pendown()
        pen.goto(x + 25, -40)


draw_cabin()

pen.color("white")
pen.pensize(2)

for i in range(8):
    x = -400 + i * 110
    y = -200 - (i % 3) * 35

    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.forward(60)

draw_rectangle(-20, -200, 40, 55, "tan")

pen.penup()
screen.mainloop()
