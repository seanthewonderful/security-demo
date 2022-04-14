import colorgram
import turtle as t
import random


colors = colorgram.extract("image.jpeg", 12)
rgb_list = []


for color in colors:
    col = color.rgb
    rgb_list.append((col[0], col[1], col[2]))

del rgb_list[:3]

def rand_color():
    return rgb_list[(random.randint(0, len(rgb_list) - 1))]
    # return random.choice(rgb_list)


tommy = t.Turtle()
tommy.shape("turtle")
tommy.color("dodgerblue")
t.colormode(255)
tommy.speed(0)
tommy.penup()
tommy.setheading(220)
tommy.forward(290)
tommy.setheading(0)


# def reset():
#     tommy.setheading(90)
#     tommy.forward(50)
#     tommy.setheading(180)
#     tommy.forward(500)
#     tommy.setheading(0)
#     draw()
    
    
# def draw():
#     for _ in range(10):
#         tommy.dot(25, rand_color())
#         tommy.fd(50)
#     if tommys_dots < 101:
#         tommys_dots += 10
#         reset()
#     else: 
#         tommy.hideturtle()
# # Error here with tommys_dots

# tommys_dots = 10
# draw()



# Instructor method:
number_of_dots = 100

for count in range(1, number_of_dots + 1):
    tommy.dot(25, rand_color())
    tommy.fd(50)
    
    if count % 10 == 0:
        tommy.setheading(90)
        tommy.forward(50)
        tommy.setheading(180)
        tommy.forward(500)
        tommy.setheading(0)
    if count == 100:
        tommy.hideturtle()

# t.Screen().exitonclick()
screen = t.Screen()
screen.exitonclick()