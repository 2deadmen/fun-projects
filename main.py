import random
from turtle import Turtle, Screen

race_on= False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet",prompt="whuch turtle will win the race..input a color")
color =["red","green","orange","yellow","blue","purple"]
y = [-100,-50,0,50,100,150]
all_turtles =[]

for i in range(0,5):
 tim = Turtle(shape="turtle")
 tim.penup()
 tim.goto(x=-230,y=y[i])
 tim.color(color[i])
 all_turtles.append(tim)

if user_bet:
    race_on = True


while race_on:
    for i in all_turtles:
        rand = random.randint(0,10)
        i.forward(rand)
        if i.xcor() > 230:
            race_on = False
            if user_bet == i.pencolor():
                print(f"you won..{i.pencolor()}  has won the race")

            else:
                print(f"you loose..{i.pencolor()} has won the race")



screen.exitonclick()
