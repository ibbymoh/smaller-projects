from turtle import Turtle,Screen
from PaddleClass import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
speed = 0.05
screen.tracer(0)

ball = Ball()
paddle1 = Paddle(350)
paddle2 = Paddle(-350)
scoreboard = Scoreboard()

screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

screen.listen()

game_is_on = True




def edge_check():
    if ball.xcor() > 370:
        scoreboard.update_player1()
        ball.start_again()
        speed = 0.05
    elif ball.xcor() < -370:
        scoreboard.update_player2()
        ball.start_again()
        speed = 0.05


while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    ball.bouncing()
    if ball.distance(paddle1) < 40 and ball.xcor() > 330:
        ball.setheading(180 - ball.heading())
        speed *= 0.95
    elif ball.distance(paddle2) <40 and ball.xcor() < -340:
        ball.setheading(180 - ball.heading())
        speed *= 0.95
    edge_check()

screen.exitonclick()