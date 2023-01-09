from turtle import Turtle

BLOCK = (((-300, 300), (-280, 300)), ((-260, 300), (-240, 300)), ((-220, 300), (-200, 300)), ((-180, 300), (-160, 300)),((-140, 300), (-120, 300)), ((-100, 300), (-80, 300)), ((-60, 300), (-40, 300)), ((-20, 300), (0, 300)))


class Block(Turtle):
    BLOCKS_LIST = []

    def __init__(self):
        super().__init__()
        for x in BLOCK:
            B = []
            for y in x:
                segment = Turtle()
                segment.penup()
                segment.color('white')
                segment.goto(y)
                segment.shape('square')
                B.append(segment)
            Block.BLOCKS_LIST.append(B)



