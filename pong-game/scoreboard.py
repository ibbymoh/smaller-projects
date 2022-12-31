
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.goto(x=0, y=220)
        self.color("white")
        self.score()
        self.hideturtle()



    def update_player1(self):
        self.player1 +=1
        self.score()

    def update_player2(self):
        self.player2 +=1
        self.score()

    def score(self):
        self.clear()
        self.write(f"{self.player1}:{self.player2}", align="center", font=('Arial', 60, 'normal'))


