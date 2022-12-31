import turtle
from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(randint(-45,45))

    def move(self):
            self.forward(10)


    def bouncing(self):
        if  290 <= self.ycor()  <= 300 or -300 <= self.ycor() <= -290:
            self.setheading(360 - self.heading())

    def start_again(self):
        old_heading = self.heading()
        self.home()
        self.setheading(old_heading + 180)
