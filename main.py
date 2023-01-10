from turtle import Screen
from Paddle import Paddle, segments
from Ball import Ball
from Block import Block
import time
move = False
game = True

def m():
    global move
    move = True


screen = Screen()
screen.tracer(0)
screen.window_width = 10
screen.bgcolor('black')
paddle = Paddle()
ball = Ball()
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
screen.onkeypress(m)
block = Block()

while game:
    time.sleep(0.01)
    ### MOVE BALL
    if move:
        ball.move()
    for x in range(len(segments)):
        if ball.distance(segments[x]) < 20:
            ball.spring_back(x)
            break

    if ball.ycor() >= 320:
        ball.spring_top()

    if ball.ycor() < -320:
        ball.goto(segments[2].xcor(), segments[2].ycor()+20)
        move = False

    if ball.xcor() < -360:
        ball.spring_left()

    if ball.xcor() > 360:
        ball.spring_right()
    screen.update()

    for x in Block.BLOCKS_LIST:
        for y in x:
            if ball.distance(y)<20:
                print(y.xcor(), y.ycor(), ball.xcor(), ball.ycor())
                for y in x:
                    y.goto(1000, 1000)
                Block.BLOCKS_LIST.remove(x)
                ball.spring_top()
screen.mainloop()

