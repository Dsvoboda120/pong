from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.nova_hra()
        l_paddle.l_defaultni_pozice()
        r_paddle.r_defaultni_pozice()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.nova_hra()
        l_paddle.l_defaultni_pozice()
        r_paddle.r_defaultni_pozice()


screen.exitonclick()