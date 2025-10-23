import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("Hitting the wall")
        ball.bounce_y()

    # detect collision with r_paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()