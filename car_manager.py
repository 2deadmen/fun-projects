import time
from turtle import Turtle,Screen

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10
MOVE = 30
screen = Screen()


class CarManager:
    def __init__(self):

        self.allcars =[]

    def lvl1(self):

        new = Turtle("square")
        colours = random.choice(COLORS)
        new.color(colours)

 #       new.shapesize(stretch_len=2)
        new.penup()
        randy = random.randint(-220,220)
        new.goto(-300,randy)
        self.allcars.append(new)
    def move(self):

        for _ in self.allcars:
           _.forward(MOVE)



