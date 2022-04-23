from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.write(f"score : {self.score}",align="center",font=("Courier",20,"normal"))


    def gameover(self):
        self.goto(0, 0)
        self.write("Game over", font=("Courier", 30, "normal"), align="center")
    def update(self):

        self.clear()
        self.score += 1
        self.write(f"score :{self.score}", align="center", font=("Courier", 24, "normal"))