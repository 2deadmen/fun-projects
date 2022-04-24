from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10
MOVE = 5



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl1()
    def lvl1(self):
        self.shape("square")

        colours = random.choice(COLORS)
        self.color("blue")
        self.shapesize(stretch_wid=1)
        self.penup()
        rand_y = random.randint(-220,220)
        self.goto(300,rand_y)

        on = True
        while on:
           self.back(MOVE)

    def lvl2(self):
        self.reset()
        self.shape("square")

        colours = random.choice(COLORS)
        self.color("red")
        self.shapesize(stretch_wid=1)
        self.penup()
        rand_y = random.randint(-220, 220)
        self.goto(300, rand_y)

        on = True
        while on:
            self.back(MOVE_INCREMENT)



