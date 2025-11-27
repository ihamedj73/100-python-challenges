import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player
player = Player()

# SCOREBOARD
scoreboard = Scoreboard()

# CarManager
car_manager = CarManager()


# EVENTS
screen.listen()
screen.onkeypress(key="Up", fun=player.go_up)
screen.onkeypress(key="Down", fun=player.go_down)
screen.onkeypress(key="Right", fun=player.go_right)
screen.onkeypress(key="Left", fun=player.go_left)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
