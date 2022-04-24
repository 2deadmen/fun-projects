from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
      def __init__(self):
            super().__init__()
            self.penup()
            self.hideturtle()
            self.goto(0,250)
            self.write("level 1",align="center",font=FONT)

      def update(self):
            self.clear()
            self.write("level 2", align="center", font=FONT)

      def gameover(self):
            self.clear()
            self.write("game over", align="center", font=FONT)


