import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move,"Up")
lvl =1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager = CarManager()
    if player.ycor() > 250:
        car_manager.lvl2()
        scoreboard.update()
        player.move()
        lvl += 1
    if player.distance(car_manager) < 10:
        game_is_on = False
        scoreboard.gameover()
    if lvl > 2 :
         game_is_on = False
         scoreboard.gameover()
         print("you won")


screen.exitonclick()