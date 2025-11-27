from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, p_position: tuple):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(p_position)

    def go_up(self):
        if self.ycor() < 270:
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -270:
            self.sety(self.ycor() - 20)
