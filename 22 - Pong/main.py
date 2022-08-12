from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong 🏓')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
game_ball = Ball()
s_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    game_ball.move()

    # Detect collision with the wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    # Detect collision with r_paddle
    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320:
        game_ball.bounce_x()
    if game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    # Detect r paddle miss
    if game_ball.xcor() > 410:
        game_ball.reset_position()
        s_board.l_point()

    # Detect l paddle miss
    if game_ball.xcor() < -410:
        game_ball.reset_position()
        s_board.r_point()


screen.exitonclick()
