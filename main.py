import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move,"Up")
lvl =1

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    car_manager.lvl1()
    car_manager.move()


    #

    if player.ycor() > 250:
        lvl += 1
        scoreboard.update()
        player.rese()

    for i in  car_manager.allcars:     #  el
        if i.distance(player) < 10:
             game_is_on = False
             scoreboard.gameover()




screen.exitonclick()
