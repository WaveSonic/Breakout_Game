from turtle import Screen
from Paddle import Paddle, segments
from Ball import Ball
from Block import Block
import time
game = True

screen = Screen()
screen.tracer(0)
screen.window_width = 10
screen.bgcolor('black')
paddle = Paddle()
ball = Ball()
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
block = Block()

while game:
    time.sleep(0.02)
    ### MOVE BALL
    ball.move()
    for x in range(len(segments)):
        if ball.distance(segments[x]) < 20:
            ball.spring_back(x)
            break

    if ball.ycor() >= 320:
        ball.spring_top()

    if ball.ycor() < -320:
        ball.goto(0, 0)

    if ball.xcor() < -360:
        ball.spring_left()

    if ball.xcor() > 360:
        ball.spring_right()
    for x in Block.BLOCKS_LIST:
        print(x)
        for y in x:
            if ball.distance(y) < 15:
                for z in x:
                    z.goto(1000, 1000)
                ball.spring_top()
            break

    for x in Block.BLOCKS_LIST:
        for y in x:
            if y.xcor() > 800:
                x.remove(y)




    screen.update()


screen.mainloop()