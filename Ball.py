from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.75)
        self.color('white')
        self.speed = 10
        self.headangle = 270
        self.goto(0, 280)

    def move(self):
        self.setheading(self.headangle)
        self.forward(self.speed)

    def spring_back(self, angle):
        if angle == 0:
            self.headangle = 130 + randint(-5, 5)
        elif angle == 1:
            self.headangle = 100 + randint(-5, 5)
        elif angle == 2:
            self.headangle = 90 + randint(-5, 5)
        elif angle == 3:
            self.headangle = 80 + randint(-5, 5)
        elif angle == 4:
            self.headangle = 50 + randint(-5, 5)

    def spring_top(self):
        self.headangle = 360 - self.headangle - randint(-5, 5)


    def spring_left(self):
        self.headangle = 180 - self.headangle - randint(-5, 5)

    def spring_right(self):
        self.headangle = 180 - self.headangle - randint(-5, 5)