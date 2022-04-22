import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
timmy = Turtle()

colors = [  (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168),  (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
timmy.speed("fastest")
for i in range(10):
    timmy.penup()
    timmy.left(90)
    timmy.forward(30)
    timmy.left(90)
    timmy.forward(300)
    timmy.right(180)
    for j in range(10):
        color = random.choice(colors)
        timmy.dot(15,color)
        timmy.penup()
        timmy.forward(30)
screen = Screen()
screen.exitonclick()