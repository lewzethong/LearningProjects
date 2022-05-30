import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.movement()

    if car_manager.cars[-1].xcor() < 220:
        for _ in range(random.randint(1, 3)):
            car_manager.create_car()

    # To remove cars from the list
    for car in car_manager.cars:
        if car.xcor() < -320:
            car_manager.cars.remove(car)

    # Detect collision with the cars
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect when crossed the road
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.reset_position()
        car_manager.stage_clear()



