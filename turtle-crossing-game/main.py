import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars_list = []
game_is_on = True
speed = 0

# initialisation of classes
scoreboard = Scoreboard()
player = Player()

# creating lots of cars at the start

for _ in range(15):
    car1 = CarManager(-300,300,speed)
    cars_list.append(car1)


# moving the player with keys

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

screen.listen()


def game_over():
    game_over_sign = Turtle()
    game_over_sign.hideturtle()
    game_over_sign.penup()
    game_over_sign.goto(0,270)
    game_over_sign.write(arg= "Game Over", align="center",font=('Arial', 8, 'bold'))

# keeping the game continuing


while game_is_on:
    for car in cars_list:
        car.move()
        if car.xcor() < -330:
            cars_list.remove(car)
        if player.distance(car) < 40:
            game_over()
            game_is_on = False

    while len(cars_list) < 20:
        car2 = CarManager(300, 450, speed)
        cars_list.append(car2)

    if player.ycor() == 280:
        scoreboard.update_score()
        player.goto((0, -280))
        speed += 1

    time.sleep(0.1)
    screen.update()
screen.exitonclick()