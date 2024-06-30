from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # 20 x 20 as default, 0.5 is a half of 20
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
