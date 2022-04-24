from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)



    def move(self):

        self.forward(MOVE_DISTANCE)

    def rese(self):

        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
