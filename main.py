from turtle import Screen
import time
from pedastriane import  PedasTrian
from blocks import Blocks
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)
score = ScoreBoard()


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
m =5
game_on = True
n = 1
while game_on:
    time.sleep(0.1)
    screen.update()
    if n % m == 0:
        blocks.random_blocks()
    blocks.blocks_move()
    blocks.remove_off_screen_blocks()
    for segment in blocks.segments:
        if segment.distance(pedastrian) < 25:
            game_on = False
            game_over()
    if pedastrian.ycor() >160:
        score.level_increase()
        pedastrian.restart()
        m = m -1
        if m == 3:
            m = m-1
        else:
            pass


    n += 1













screen.exitonclick()
