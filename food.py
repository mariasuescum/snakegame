from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)