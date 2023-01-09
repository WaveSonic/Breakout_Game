from turtle import Turtle
START_POS = ((-40, -280), (-20, -280), (0, -280), (20, -280), (40, -280))
segments = []

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        for x in START_POS:
            segment = Turtle()
            segment.shape('square')
            segment.color('white')
            segment.penup()
            segment.goto(x)
            segments.append(segment)

    def move_left(self):
        if segments[0].xcor() >= -340:
            for x in segments:
                x.setheading(180)
                x.forward(50)

    def move_right(self):
        if segments[-1].xcor() <= 340:
            for x in segments:
                x.setheading(0)
                x.forward(40)