from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,xrange1,xrange2,level):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3,stretch_wid=1.5)
        self.color(choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(randint(xrange1,xrange2),randint(-250,250))
        self.level = level



    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level)


    def additional_cars(self):
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1.5)
        self.color(choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(randint(300,320), randint(-250, 250))
        self.level = 0