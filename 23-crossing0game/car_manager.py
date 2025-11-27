
import random
import select
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 2
# STREET_POSITIONS = [-240, -]

y_positions = [-240, -219, -198, -177, -156, -135, -114, -93, -
               72, -51, -30, -9, 12, 33, 54, 75, 96, 117, 138, 159, 180, 201, 222]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() < -330:
                self.delete_car(car)
            else:
                car.backward(self.car_speed)

    def delete_car(self, car):
        self.all_cars.remove(car)
        del car

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
