from ctypes.wintypes import RGB
from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
timmy.shape("turtle")
timmy.color("dodgerblue")
colormode(255)
timmy.speed(0)

# Square
# for _ in range(4):
#     timmy.forward(150)
#     timmy.left(90)

# Dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# for _ in range(7):
    
# timmy.pencolor("red")
# timmy.circle(50, 360, 3)
# timmy.pencolor("green")
# timmy.circle(60, 360, 4)
# timmy.pencolor("random")
# timmy.circle(70, 360, 5)
# timmy.pencolor()
# timmy.circle(80, 360, 6)
# timmy.pencolor()
# timmy.circle(90, 360, 7)
# timmy.pencolor()
# timmy.circle(110, 360, 8)
# timmy.pencolor()
# timmy.circle(120, 360, 9)
# timmy.pencolor()
# timmy.circle(130, 360, 10)


num_sides = 3
colors = ["red", "green", "blue", "brown", "gray", "orange", "gold", "aqua", "deep pink", "blue violet"]
rotation = [0, 90, 180, 270]


def draw_shapes(num_sides, color):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.pencolor(color)
        timmy.forward(100)
        timmy.right(angle)
        

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, b, g)

head_dir = 0

# for _ in range(72):
#     timmy.color(random_color())
#     timmy.circle(180)
#     timmy.setheading(head_dir)
#     head_dir += 5
    

# for _ in range(100):
#     timmy.speed(0)
#     # timmy.color(colors[random.randint(0, (len(colors) - 1))])
#     timmy.color(random_color())
#     timmy.width(10)
#     timmy.forward(40)
#     timmy.setheading(rotation[random.randint(0, (len(rotation) - 1))])


# for side in range(3, 11):
#     rand = random.randint(0, (len(colors) - 1))
#     color = colors[rand]
#     draw_shapes(side, color)



screen = Screen()
screen.exitonclick()

