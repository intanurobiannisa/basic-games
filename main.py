from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Bricks
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -220))
ball = Ball((0, -210))
scoreboard = Scoreboard()
wall = Bricks()
loose = 0

screen.listen()
screen.onkey(paddle.right,"Right")
screen.onkey(paddle.left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # control the screen.tracer
    ball.move()

    if ball.xcor() > 370 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 70 and ball.ycor() > 190 or ball.distance(paddle) < 70 and ball.ycor() < -190:
        ball.bounce_y()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -350:
        ball.reset_position()
        paddle.goto(0, -220)
        loose += 1

    if loose >= 2 or len(wall.bricks) == 0:
        game_is_on = False
        scoreboard.game_over()

    for brick in wall.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1

            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                wall.bricks.remove(brick)
                scoreboard.create_new_score()

            # detect collision from left and right
            if ball.xcor() < brick.left_wall or ball.xcor() > brick.right_wall:
                ball.bounce_x()

            # detect collision from bottom and top
            if ball.ycor() < brick.bottom_wall or ball.ycor() > brick.upper_wall:
                ball.bounce_y()

screen.exitonclick()