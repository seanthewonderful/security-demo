from turtle import Turtle, Screen


tammy = Turtle()
screen = Screen()


def move_forwards():
    tammy.forward(10)


def move_backwards():
    tammy.backward(10)
    
    
def move_left():
    tammy.left(10)
    

def move_right():
    tammy.right(10)
    
    
def clear():
    tammy.clear()
    # tammy.reset()
    
    
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(clear, "c")
screen.exitonclick()