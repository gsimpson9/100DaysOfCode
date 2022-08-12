from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        random_y = random.randint(-240, 240)
        new_car.goto(x=300, y=random_y)
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









