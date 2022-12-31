from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self,starting_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(x=starting_x, y=0)

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.backward(20)
