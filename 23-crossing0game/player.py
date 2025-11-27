import time
from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("brown")
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -300:
            self.backward(MOVE_DISTANCE)

    def go_right(self):
        x_pos = self.xcor()
        if x_pos < 280:
            self.setposition(x=x_pos + MOVE_DISTANCE, y=self.ycor())

    def go_left(self):
        x_pos = self.xcor()
        if x_pos > -280:
            self.setposition(x=x_pos - MOVE_DISTANCE, y=self.ycor())

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
