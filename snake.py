from turtle import Turtle,Screen
START = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]
    def create_snake(self):
        for i in START:
            self.add_segment(i)
    def add_segment(self,i):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(i)
        self.segments.append(snake)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):

            for segnum in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segnum - 1].xcor()
                new_y = self.segments[segnum - 1].ycor()
                self.segments[segnum].goto(new_x, new_y)
            self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)