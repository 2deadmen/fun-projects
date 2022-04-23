from turtle import Screen
from paddle1 import Paddle1
from paddle2 import Paddle2
from ball import Ball
from score import Score


score = Score()
ball = Ball()
screen = Screen()
paddle1 = Paddle1()
paddle2 = Paddle2()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.listen()


screen.onkey(paddle1.moveup,"Up")
screen.onkey(paddle1.movedown,"Down")
screen.onkey(paddle2.moveup, "w")
screen.onkey(paddle2.movedown, "s")
is_on = True
while is_on:

  if ball.distance(paddle1) < 10 or ball.distance(paddle2) < 10:
     ball.reflect()
     score.update()
  elif ball.ycor() > 280 or ball.ycor() < -280:
      ball.reflect()
  elif ball.xcor() > 380 or ball.xcor() < - 380:
      score.gameover()





is_yes= True
while is_yes:
    screen.update()

















screen.exitonclick()