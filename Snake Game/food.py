from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # when inheriting, creating & calling an object from copied class isnt needed; just "self"
        self.pu()
        self.color("red")
        self.shapesize(.5, .5, )
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x=x, y=y)

    def morefood(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x=x, y=y)



