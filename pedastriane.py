from turtle import Turtle

class PedasTrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x=0,y=-250)
        self.left(90)


    def move_forward(self):
        self.forward(10)
