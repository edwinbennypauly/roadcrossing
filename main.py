from turtle import Screen
import time
from pedastriane import  PedasTrian
from blocks import Blocks
screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)

def game_over():
    screen.clear()
    pedastrian.end()
    screen.update()
def game_won():
    screen.clear()
    pedastrian.won()
    screen.update()


pedastrian = PedasTrian()
blocks =Blocks()


screen.listen()

screen.onkey(key="Up",fun=pedastrian.move_forward)

game_on = True
n = 5
while game_on:
    time.sleep(0.1)
    screen.update()
    if n % 5 == 0:
        blocks.random_blocks()
    blocks.blocks_move()
    blocks.remove_off_screen_blocks()
    for segment in blocks.segments:
        if segment.distance(pedastrian) < 25:
            game_on = False
            game_over()
    if pedastrian.ycor() >160:
        game_on = False
        game_won()
    n += 1













screen.exitonclick()
