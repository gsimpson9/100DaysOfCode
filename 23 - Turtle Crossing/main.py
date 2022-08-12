import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import ScoreBoard

tim = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(tim.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 6:
        car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(tim) < 25:
            game_is_on = False
            score_board.game_over()

    # Detect when the player has reached the other side
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        score_board.score_point()

screen.exitonclick()

