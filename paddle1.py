from turtle import Turtle


class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=6,stretch_len=1)
        self.penup()
        self.goto(380,0)


    def moveup(self):
     next_y =self.ycor() + 40
     if self.ycor() < 280:
        self.goto(380, next_y)


    def movedown(self):
      next_y = self.ycor() - 40
      if self.ycor() > -280:
         self.goto(380, next_y)


