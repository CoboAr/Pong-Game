from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# Create Right paddle, Left paddle, Ball, and Scoreboard objects
r_puddle = Paddle((350,0))
l_puddle = Paddle((-350,0))
scoreboard = Scoreboard()
ball = Ball()
# Eventhandler functions to move right and left paddles up/down
screen.listen()
screen.onkey(r_puddle.go_up_r,"Up")
screen.onkey(r_puddle.go_down_r,"Down")
screen.onkey(l_puddle.go_up_l,"w")
screen.onkey(l_puddle.go_down_l,"s")
# Start the game
game_is_on = True
while game_is_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

    # Detect collision with right and left puddle
    if ball.distance(r_puddle)<50 and ball.xcor()>320 or ball.distance(l_puddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect Right paddle misses
    if  ball.xcor()>380:
        ball.restart()
        scoreboard.l_point()

    # Detect Left puddle misses
    if ball.xcor()<-380:
        ball.restart()
        scoreboard.r_point ()

screen.exitonclick()