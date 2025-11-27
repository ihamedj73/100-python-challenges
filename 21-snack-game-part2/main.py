import time
from turtle import Screen
from snack import Snack
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)


snack = Snack()
food = Food()
scoreBoard = Scoreboard()

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

    # Detect collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        scoreBoard.increase_score()

    # Detect collision with wall.
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        scoreBoard.reset()
        snack.reset()

        # Detect collision with tail.
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 10:
            scoreBoard.reset()
            snack.reset()


screen.exitonclick()
