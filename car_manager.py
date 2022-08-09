import random
from turtle import Turtle, colormode


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        
        colormode(255)
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.goto(280,random.randint(-250,280))
        self.setheading(180)
        cars.append(self)
        

    def car_forward(self):
        for element in cars:
            element.forward(MOVE_INCREMENT)
    def get_cars(self):
        return cars

    def reset_level(self):
        self.clear()