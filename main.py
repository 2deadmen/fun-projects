import turtle

import pandas as pandas

screen = turtle.Screen()
img ="blank_states_img.gif"
screen.addshape(img)
screen.setup(width=700,height=500)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")

states = 0
on =True
while on:
   user_input =screen.textinput(title=f" score:{states}/50",prompt="guess a state")

   file_data =data[data.state == user_input]
   compare_data = file_data["state"].to_list()

   if  user_input in compare_data:
        new = turtle.Turtle("circle")
        new.hideturtle()
        new.penup()
        x_list =file_data["x"].to_list()
        y_list = file_data["y"].to_list()
        x =int(x_list[0])
        y =int(y_list[0])
        new.goto(x,y)
        new.write(compare_data[0],align="center",font=("Courier",5,"normal"))
        states += 1

   else:
       pass
   if states == 50:
            on =False
            won = turtle.Turtle()
            won.hideturtle()
            won.write("you won",align="center",font=("Courier",30,"normal"))



turtle.mainloop()

