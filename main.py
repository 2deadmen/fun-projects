from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake-game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    if snake.head.distance(food) < 15:
     food.refresh()
     snake.extend()
     scoreboard.update()

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.gameover()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()






screen.exitonclick()