import time
from turtle import Turtle, Screen
from snack import Snack


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)


snack = Snack()

screen.listen()
screen.onkey(key="Up", fun=snack.up)
screen.onkey(key="Down", fun=snack.down)
screen.onkey(key="Left", fun=snack.left)
screen.onkey(key="Right", fun=snack.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()

screen.exitonclick()
