from turtle import Turtle
import time
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(0.5)
        self.penup()
        self.goto(0,0)
        self.move()

    def move(self):
        game_on = True
        while game_on:
         self.forward(10)
         time.sleep(0.1)

    def reflect(self):
        rand_angle = random.randint(60,120)
        self.right(rand_angle)
