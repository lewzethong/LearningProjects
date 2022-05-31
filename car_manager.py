from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.movement_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.color(random.choice(COLORS))
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.pu()
            new_cars.setheading(180)
            new_cars.goto(300, random.choice(range(-250, 280, 30)))
            self.cars.append(new_cars)

    def movement(self):
        for car in self.cars:
            car.forward(self.movement_speed)

    def stage_clear(self):
        self.movement_speed += MOVE_INCREMENT




