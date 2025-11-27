import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.y_move = random.choice([-10, 10])
        self.x_move = random.choice([-10, 10])
        self.move_speed = 0.1

    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
