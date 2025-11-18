import random
from turtle import Turtle, Screen, colormode

colormode(255)
tim = Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
color_list = [(236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121,
                                               86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45,
                                                 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27,
                                                            68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tim.width(20)


def set_position(i):
    tim.setposition(-250, -250 + i * 50)


def move():
    tim.dot(20, random.choice(color_list))

    tim.forward(50)


for i in range(10):
    set_position(i)
    for _ in range(10):
        move()

screen = Screen()
screen.exitonclick()
