from turtle import  Turtle
import  random

class Blocks():
    def __init__(self):
        self.segments = []

    def random_blocks(self):
        colours = ["black","blue","yellow","green","orange","red"]
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.shapesize(stretch_wid=1, stretch_len=3)
        new_turtle.color(random.choice(colours))
        new_turtle.left(180)
        new_turtle.penup()
        new_turtle.goto(x=300, y= random.randint(-150, 150))
        self.segments.append(new_turtle)

    def blocks_move(self):
        for block in self.segments:
            block.forward(10)
    def remove_off_screen_blocks(self):
        for block in self.segments:
            if block.xcor() < -280:
                block.clear()


