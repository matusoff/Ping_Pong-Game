from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
r_score = Score((300, 270))
l_score = Score((-300, 270))


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "s")
screen.onkey(l_paddle.down, "x")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
#Detect collision with top and bottom walls (then ball will change direction)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_dir_y()
        

    #Detect collision with right and left paddles 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.change_dir_x()
    

    #Detect R paddle miss a ball and update score    
    elif ball.xcor() > 380:
        ball.reset_position()
        l_score.update_score()
    # elif r_score ==10:
    #     score.game_over()
    #     game_is_on = False
    
    #Detect L paddle miss a ball and update score        
    elif ball.xcor() < -380:
        ball.reset_position()
        r_score.update_score()
    # elif l_score ==10:
    #     score.game_over()
    #     game_is_on = False
       

    # #Game Over
    # elif r_score or l_score == 10:
    #     game_is_on = False
    #     r_score.game_over() or l_score.game_over()

screen.exitonclick()