import turtle as t
import random
s = t.Screen()
s.setup(height=600, width=800)
s.bgcolor('white')
s.tracer(0)
# Left_Paddle
left_paddle = t.Turtle()
left_paddle.shape('square')
left_paddle.speed(0)
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color('blue')
left_paddle.penup()
left_paddle.goto(-350, 0)
# right_Paddle
right_paddle = t.Turtle()
right_paddle.shape('square')
right_paddle.speed(0)
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color('red')
right_paddle.penup()
right_paddle.goto(350, 0)
# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball_dx = 0.5
ball_dy = 0.5
# score var
k1=0
k2=0

# score board
scoreboard = t.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.shapesize(stretch_wid=2, stretch_len=10)
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-110, 275)
#start msg
msg = t.Turtle()
msg.speed(0)
msg.color("black")
msg.shapesize(stretch_wid=3, stretch_len=15)
msg.penup()
msg.hideturtle()
msg.goto(-130, 0)
msg.write("press space to start", align="left", font=("Arial", 28, "normal"))
# moving left paddle
def left_paddle_up():
    if left_paddle.ycor() + 40 < 290:
        left_paddle.sety(left_paddle.ycor() + 50)


def left_paddle_down():
    if left_paddle.ycor() - 40 > -290:
        left_paddle.sety(left_paddle.ycor() - 50)
def score(k1,k2):


    ch1=str(k1)
    ch2=str(k2)
    scoreboard.clear()

    scoreboard.write("player: "+ch1+"    "+"computer: "+ch2, align="left", font=("Arial", 18, "normal"))

    
def start_game():
    msg.clear()
    



    
s.listen()
s.onkeypress(start_game, "space")
    
s.onkeypress(left_paddle_up, "Up")
s.onkeypress(left_paddle_down, "Down")
score(0,0)
    # game loop
while True:
    s.update()
    
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball_dy *= -1
    if ball.xcor() < -390 or ball.xcor() > 390:
        if ball.xcor()>390 :
            k1=k1+1
        else:
            k2=k2+1
        right_paddle.goto(350, 0)
        left_paddle.goto(-350, 0)
        ball.goto(0, 0)
        score(k1,k2)
        ball_dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and \
            (left_paddle.ycor() + 60 > ball.ycor() > left_paddle.ycor() - 60):
        ball_dx *= -1
    if (ball.xcor() > 340) and (ball.xcor() < 350) and \
            (right_paddle.ycor() + 60 > ball.ycor() > right_paddle.ycor() - 60):
        ball_dx *= -1

    if ball_dx > 0:
        if ball_dy > 0:
            if right_paddle.ycor() + 30 < 290 :
                while right_paddle.ycor() + 30 < ball.ycor():
                    right_paddle.sety(right_paddle.ycor() + 20)
        if ball_dy < 0:
            if right_paddle.ycor() - 30 > -290 :
                while right_paddle.ycor() - 30 > ball.ycor() :
                    right_paddle.sety(right_paddle.ycor() - 20)



