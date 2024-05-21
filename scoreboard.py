from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.write(arg=f"Level {self.n}",align="left",font=("Arial",13,"normal"))


    def level_increase(self):
        self.n += 1
        self.clear()
        self.write(arg=f"Level {self.n}",align="left",font=("Arial",13,"normal"))
