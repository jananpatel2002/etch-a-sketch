from turtle import Turtle, Screen

tim = Turtle()


def move_forward_10():
    tim.forward(10)


def move_backwards_10():
    tim.back(10)


def clear_screen():
    tim.penup()
    tim.setpos(0, 0)
    tim.clear()
    tim.setheading(0)
    tim.pd()


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward_10)
screen.onkey(key="s", fun=move_backwards_10)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
