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

    car_manager.create_car()
    car_manager.movement()

    # To remove cars from the list
    for car in car_manager.cars:
        if car.xcor() < -320:
            car_manager.cars.remove(car)

    # Detect collision with the cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when crossed the road
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.reset_position()
        car_manager.stage_clear()

screen.exitonclick()



