from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("black")
        self.setposition((-280, 260))
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self._update_scoreboard()

    def game_over(self):
        self.setposition((0, 0))
        self.write("Game over!", align='center', font=FONT)
